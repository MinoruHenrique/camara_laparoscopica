import cv2
import image_processing

def track_callback(val):
    global KERNEL_SIZE, SIGMAX, HE
    kernel_size = cv2.getTrackbarPos("kernel_size", window_name)
    sigmax = cv2.getTrackbarPos("sigmax", window_name)
    heq = cv2.getTrackbarPos("histogram_equalization", window_name)
    
    if(kernel_size%2!=0):
        KERNEL_SIZE = kernel_size
    SIGMAX = sigmax
    HE = heq
    print(KERNEL_SIZE, SIGMAX, HE)

#gaussian filter parameters
KERNEL_SIZE = 5
SIGMAX = 0
HE = 1
frame_name = "frames"
window_name = "processed_image"




if __name__=="__main__":

    vid = cv2.VideoCapture(0)
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.namedWindow(frame_name, cv2.WINDOW_NORMAL)

    cv2.createTrackbar("kernel_size",window_name, 0, 15, track_callback)
    cv2.createTrackbar("sigmax", window_name, 0, 20, track_callback)
    cv2.createTrackbar("histogram_equalization", window_name, 0, 1, track_callback)

    cv2.resizeWindow(frame_name, 180,180)
    cv2.resizeWindow(window_name, 180,180)
    while(True):
      
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
    
        processed = frame.copy()
        if(HE):
            processed = image_processing.HE(processed)
        processed = image_processing.gaussian_filter(processed, KERNEL_SIZE, SIGMAX)
        # Display the resulting frame
        cv2.imshow(frame_name, frame)
        cv2.imshow(window_name, processed)
    
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
