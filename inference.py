from commons import get_tensor, get_model
import json

with open('cat_to_name.json') as f:
    cat_to_name = json.load(f)

with open('class_to_idx.json') as f:
    class_to_idx = json.load(f)

idx_to_class = {v: k for k, v in class_to_idx.items()}

model = get_model('project_checkpoint.pth')


def get_flower_name(image_bytes, file):
    tensor = get_tensor(image_bytes, file)
    outputs = model.forward(tensor)
    _, prediction = outputs.max(1)
    category = prediction.item()
    print(category)
    class_idx = idx_to_class[category]
    flower_name = cat_to_name[class_idx]
    # file.
    # save('flowers_1.jpg')
    flower_name = flower_name[0].upper() + flower_name[1:]
    return category, flower_name
