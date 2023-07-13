;; Auto-generated. Do not edit!


(when (boundp 'pub_value::StringArray)
  (if (not (find-package "PUB_VALUE"))
    (make-package "PUB_VALUE"))
  (shadow 'StringArray (find-package "PUB_VALUE")))
(unless (find-package "PUB_VALUE::STRINGARRAY")
  (make-package "PUB_VALUE::STRINGARRAY"))

(in-package "ROS")
;;//! \htmlinclude StringArray.msg.html


(defclass pub_value::StringArray
  :super ros::object
  :slots (_data ))

(defmethod pub_value::StringArray
  (:init
   (&key
    ((:data __data) (let (r) (dotimes (i 0) (push "" r)) r))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string[] _data
    (apply #'+ (mapcar #'(lambda (x) (+ 4 (length x))) _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string[] _data
     (write-long (length _data) s)
     (dolist (elem _data)
       (write-long (length elem) s) (princ elem s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (make-list n))
     (dotimes (i n)
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setf (elt _data i) (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
     ))
   ;;
   self)
  )

(setf (get pub_value::StringArray :md5sum-) "cce5a364f3a3be12c9722c6dcad2fa94")
(setf (get pub_value::StringArray :datatype-) "pub_value/StringArray")
(setf (get pub_value::StringArray :definition-)
      "string[] data

")



(provide :pub_value/StringArray "cce5a364f3a3be12c9722c6dcad2fa94")


