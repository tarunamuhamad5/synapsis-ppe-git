from ultralytics import YOLO

model = YOLO("model.pt")
model.to("cuda")

# source = 0 is internal camera, 1 for external camera
result = model(source=0, show=True, conf=0.35, save=True, device=0)
