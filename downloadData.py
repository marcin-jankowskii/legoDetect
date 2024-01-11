from roboflow import Roboflow

rf = Roboflow(api_key="U22b93cUm1F7NFbp9wCj")
project = rf.workspace("poltechnika-gdaska").project("lego_full")
dataset = project.version(1).download("yolov8")
