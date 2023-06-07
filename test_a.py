import torch
import PIL


model = torch.hub.load("./", "custom", path="yolov5s.pt", source="local")
model.to("cuda")
image = "./data/images/bus.jpg"
results = model(image)
print(results.pred)
imgarray = results.render()[0]
print(imgarray.shape)
img = PIL.Image.fromarray(imgarray)  # 从array转换为PILimage
img.show()
