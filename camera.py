import cv2

if __name__=="__main__":
    vid = cv2.VideoCapture(0)
    while(True):
      
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        frame = cv2.resize(frame, (540,360))  
        
        cv2.imshow('frame', frame)

        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()