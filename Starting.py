import cv2
import numpy as np

class My_Magic:

    def __init__(self, file_name):
        self.__image = cv2.imread(file_name)
        self.__pixel_list = []

    def __get_image(self):
        return self.__image

    def __get_pixel_lst(self):
        height, width, channels = self.__get_image().shape
        if int(width) != 52:
            raise Exception

        for i in range(int(52)):
            slice = self.__get_image()[0:height, i:i + 1]
            self.__pixel_list.append(slice)
        return self.__pixel_list

    def shuffle(self, shuffle_type):
        pixel_lst = []
        try:
            pixel_lst = self.__get_pixel_lst()
        except Exception:
            print("There is a problem - I think that the image width is not 52...")
        first_half = pixel_lst[0:26]
        second_half = pixel_lst[26:]
        new_pixel_lst = []
        if shuffle_type == "0":
            for i in range(26):
                new_pixel_lst.append(first_half[i])
                new_pixel_lst.append(second_half[i])
        elif shuffle_type == "1":
            for i in range(26):
                new_pixel_lst.append(second_half[i])
                new_pixel_lst.append(first_half[i])
        elif shuffle_type == "2":
            self.__make_new_image()
        else:
            new_shuffle_type = input("Dude, what? I said, only 0, 1, or 2! try again: ")
            self.shuffle(new_shuffle_type)

        self.__pixel_list = new_pixel_lst

    def __make_new_image(self):
        img_in_process = self.__pixel_list[0]
        for i in range(51):
            img_in_process = np.concatenate((img_in_process, self.__pixel_list[i + 1]), axis=1)
        cv2.imwrite("New_Image.png", img_in_process)
        cv2.imshow("Vuala!", img_in_process)
        cv2.waitKey(0)



if __name__ == '__main__':
    file_name = str(input("Hey Itai! Ya gever, give me your file name please: "))
    my_magic = My_Magic(file_name)
    shuffling_type = "0"
    while shuffling_type != "2":
        shuffling_type = input("Sababa, how to shuffle? for infaro press 1, for outfaro press 0, to finish shuffling"
                               " press 2: ")
        my_magic.shuffle(shuffling_type)
    print("\nOk the new image is now save in the directory.\nTo start again, please click on the green triangle."
          "\nBayush! :)")
