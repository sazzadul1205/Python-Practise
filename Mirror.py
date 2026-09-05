import os
import cv2


base = input("Enter base folder: ").strip()

images = os.path.join(base, "Images")
labels = os.path.join(base, "Labels")

if not os.path.isdir(images):
    print("Images folder not found.")
    exit()

if not os.path.isdir(labels):
    print("Labels folder not found.")
    exit()


images_swap = os.path.join(base, "Images-swap")
labels_swap = os.path.join(base, "Labels-swap")

os.makedirs(images_swap, exist_ok=True)
os.makedirs(labels_swap, exist_ok=True)


valid_extensions = (".png")


for filename in os.listdir(images):

    if not filename.lower().endswith(valid_extensions):
        continue

    name = os.path.splitext(filename)[0]

    image_path = os.path.join(images, filename)
    label_path = os.path.join(labels, name + ".txt")

    if not os.path.isfile(label_path):
        print("Label not found:", filename)
        continue


    image = cv2.imread(image_path)
    

    if image is None:
        print("Could not Find image:", filename)
        continue


    flipped = cv2.flip(image, 1)


    with open(label_path, "r") as f:
        lines = f.readlines()


    new_labels = []

    for line in lines:

        parts = line.strip().split()

        if len(parts) != 5:
            print("Invalid label:", line.strip())
            continue

        cls = parts[0]
        x = float(parts[1])
        y = float(parts[2])
        w = float(parts[3])
        h = float(parts[4])

        x = 1 - x

        new_labels.append(f"{cls} {x} {y} {w} {h}")


    output_image = os.path.join(
        images_swap,
        name + "-swap.png"
    )

    output_label = os.path.join(
        labels_swap,
        name + "-swap.txt"
    )


    cv2.imwrite(output_image, flipped)

    with open(output_label, "w") as f:
        f.write("\n".join(new_labels))

    print("Processed:", filename)


print("Finished.")
print("Images:", images_swap)
print("Labels:", labels_swap)