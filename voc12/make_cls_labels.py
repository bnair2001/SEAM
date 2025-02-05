import argparse
import data
import numpy as np

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--train_list", default='train_list.txt', type=str)
    parser.add_argument("--val_list", default='valid_list.txt', type=str)
    parser.add_argument("--out", default="cls_bb_labels.npy", type=str)
    parser.add_argument("--voc12_root", required=True, type=str)
    args = parser.parse_args()

    # img_name_list = data.load_img_name_list(args.train_list)
    # img_name_list.extend(data.load_img_name_list(args.val_list))
    img_name_list = data.load_img_name_list("bb_list.txt")
    label_list = data.load_image_label_list_from_xml(img_name_list, args.voc12_root)

    d = dict()
    for img_name, label in zip(img_name_list, label_list):
        d[img_name] = label

    np.save(args.out, d)