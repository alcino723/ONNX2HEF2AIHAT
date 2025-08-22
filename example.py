import numpy as np
import hailo_platform as hpf
import cv2

hef = hpf.HEF("YOUR_MODEL_NAME.hef")

with hpf.VDevice() as target:
    configure_params = hpf.ConfigureParams.create_from_hef(hef, interface=hpf.HailoStreamInterface.PCIe)
    network_group = target.configure(hef, configure_params)[0]
    network_group_params = network_group.create_params()

    input_vstream_info = hef.get_input_vstream_infos()[0]
    output_vstream_info = hef.get_output_vstream_infos()[0]

    input_vstreams_params = hpf.InputVStreamParams.make_from_network_group(
        network_group, quantized=True, format_type=hpf.FormatType.UINT8
    )
    output_vstreams_params = hpf.OutputVStreamParams.make_from_network_group(
        network_group, quantized=True, format_type=hpf.FormatType.UINT8
    )

    input_shape = input_vstream_info.shape
    output_shape = output_vstream_info.shape

    print(f"Input shape: {input_shape}, Output shape: {output_shape}")

    # OpenCV Video Capture -
    cap = cv2.VideoCapture(8, cv2.CAP_V4L2)
    cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30.0)
    cap.set(cv2.CAP_PROP_CONVERT_RGB, 1)

    try:
        with network_group.activate(network_group_params):
            with hpf.InferVStreams(network_group, input_vstreams_params, output_vstreams_params) as infer_pipeline:
                print("Starting inference loop. Press Ctrl+C to exit.")

                input_buffer = np.empty((1, input_shape[0], input_shape[1], 3), dtype=np.uint8)

                while True:
                    ret, frame = cap.read()
                    if not ret:
                        print("Failed to read frame from camera.")
                        break
                    
                    resized_frame = cv2.resize(frame, (input_shape[1], input_shape[0]), dst=input_buffer[0])
                    input_data = {input_vstream_info.name: np.expand_dims(resized_frame, axis=0)}
                    results = infer_pipeline.infer(input_data)
                    output_data = results[output_vstream_info.name] 

                    # Example Post Process
                    #output_data = np.argmax(output_data[0], axis=-1).astype(np.uint8) 

    except KeyboardInterrupt:
        print("\nInterrupted by user. Shutting down")
    finally:
        cap.release()