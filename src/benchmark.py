def benchmark_detection(detect_function, video_path):
    import cv2
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    start_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        detect_function(frame)

    cap.release()
    total_time = time.time() - start_time
    fps = frame_count / total_time
    print(f"Processed {frame_count} frames in {total_time:.2f} seconds ({fps:.2f} FPS).")