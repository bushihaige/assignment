#python3 ./my_detection_pic.py ~/jetson-inference/examples/test_data/2096.jpg ~/jetson-inference/examples/test_data/2398.jpg 

# my-detection.py  —— 图片输入版本
import sys
import jetson_inference as ji
import jetson_utils as ju

if len(sys.argv) < 2:
    print("Usage: python3 my-detection.py <img1> [img2 ...]")
    sys.exit(1)

net = ji.detectNet("ssd-mobilenet-v2", threshold=0.5)

for i, p in enumerate(sys.argv[1:], 1):
    img = ju.loadImage(p)
    dets = net.Detect(img)
    for d in dets:
        print(f"ClassID:{d.ClassID}, Confidence:{d.Confidence:.3f}, "
              f"Left:{d.Left:.1f}, Top:{d.Top:.1f}, Right:{d.Right:.1f}, Bottom:{d.Bottom:.1f}, "
              f"Width:{d.Width:.1f}, Height:{d.Height:.1f}, Area:{d.Area:.0f}, "
              f"Center:({d.Center[0]:.1f},{d.Center[1]:.1f})")
    ju.saveImage(f"det_out_{i}.jpg", img)
