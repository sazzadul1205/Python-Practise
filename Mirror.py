import os
from PIL import Image

def main():
    base = input("Enter base folder (must contain 'Images' and 'Labels' subfolder's): ").strip()
    
    images_in = os.path.join(base, "Images")
    labels_in = os.path.join(base, "Labels")
    
    if not os.path.isdir(images_in):
        print("ERROR: 'Images' folder not found.")
        return
    if not os.path.isdir(labels_in):
        print("ERROR: 'Labels' folder not found.")
        return

    images_out = os.path.join(base, "Images-swap")
    labels_out = os.path.join(base, "Labels-swap")
    os.makedirs(images_out, exist_ok=True)
    os.makedirs(labels_out, exist_ok=True)

    valid_ext = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")
    
    for file in os.listdir(images_in):
        if not file.lower().endswith(valid_ext):
            continue
        
        name = os.path.splitext(file)[0]
        img_path = os.path.join(images_in, file)
        lbl_path = os.path.join(labels_in, name + ".txt")
        
        if not os.path.isfile(lbl_path):
            print(f"Skipping {file} – label not found.")
            continue
        
        with open(lbl_path, "r") as f:
            lines = f.readlines()
        
        img = Image.open(img_path)
        flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
        
        out_img = os.path.join(images_out, name + "-swap.png")
        out_txt = os.path.join(labels_out, name + "-swap.txt")
        
        new_lines = []
        for line in lines:
            parts = line.strip().split()
            if len(parts) != 5:
                print(f"Invalid label line in {lbl_path}: {line.strip()}")
                continue
            cls, x, y, w, h = parts[0], float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])
            new_x = 1.0 - x
            new_lines.append(f"{cls} {new_x:.6f} {y:.6f} {w:.6f} {h:.6f}")
        
        flipped.save(out_img)
        with open(out_txt, "w") as f:
            f.write("\n".join(new_lines) + "\n")
        print(f"Processed: {file}")
    
    print("All done.")
    print(f"Flipped images: {images_out}")
    print(f"Flipped labels: {labels_out}")

if __name__ == "__main__":
    main()