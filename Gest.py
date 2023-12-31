import torch

# Model
model=torch.load('D:\mini project\sem5\hand_gesture\yolov5-master/runs/train\exp\weights/best.pt')

# Images
imgs=['E:\Study\currency.jpg']

# Inference
results = model(imgs)

# Results
results.print()
results.save()  # or .show()
results.show()
results.xyxy[0]  # img1 predictions (tensor)
results.pandas().xyxy[0]