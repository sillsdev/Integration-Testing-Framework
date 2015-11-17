import re #regex
import threading
import sys # May not be used
import os
import shutil #for moving files
from sikuli import *
from javax.swing import (ImageIcon, JOptionPane)
#/\ for show_PNG
from javax.swing import (JFrame, JPanel, JLabel, ImageIcon, BorderFactory, JButton,WindowConstants)
from java.awt import Color
#/\ last 2 for show_PNG2, may be removed.
#Settings.ActionLogs = False
Settings.InfoLogs = False

class ImageUpdater:
    def __init__(self, test_name=""):
        self.myOS = Env.getOS()
        print(self.myOS)

        self.test = test_name

        #manually made new OS and temp/working folders
        # TODO Automate.
        self.my_path = "/home/vagrant/Integration-Testing-Framework/image_updater.sikuli"
        self.old_scripts_path = "/home/vagrant/Integration-Testing-Framework/sikuli/"
        self.new_scripts_path = "/home/vagrant/Integration-Testing-Framework/sikuli_windows/"
        self.temp_scripts_path = self.my_path+"/Integration-Testing-Framework/sikuli/"

        self.base_path_length = len(self.old_scripts_path)
        if self.myOS == OS.LINUX:
            self.temp_path_length = len(self.temp_scripts_path)
        elif self.myOS == OS.WINDOWS:
            self.temp_path_length = len(self.temp_scripts_path)+2
        else:
            popup("unsupported OS","Error")
        self.mwd = os.path.dirname(test_name)
        self.pwd = self.mwd[self.temp_path_length:]

        self.my_event = threading.Event()
        self.my_event.set()
        self.my_event2 = threading.Event()
        self.my_event2.set()
        self.showing_PNG = False
        self.image_name = "-"
        self.image_path = "-"
        self.capture_path = "-"
        self.line_text = "-"
        self.similarity = "default"
        self.show_prompt = True

    def __del__(self):
        #self.check_images()
        pass


    def make_sub_dir(self, directory_name):
        if not os.path.exists(self.temp_scripts_path+directory_name):
            #print("Making directory "+self.temp_scripts_path+directory_name)
            os.makedirs(os.path.join(self.temp_scripts_path,directory_name))

    def recursive_make(self, folder=None):
        if folder == None:
            folder = self.old_scripts_path
        for foldername, subfolders, filenames in os.walk(folder):
            if subfolders :
                for subfolder in subfolders:
                    #print("folder ="+foldername)
                    #print("subfolder ="+subfolder)
                    #print("working_folder =" +os.path.join(foldername,subfolder))
                    self.make_sub_dir(os.path.join(foldername[self.base_path_length:],subfolder))
                    #if folder does not contain images copy contents
                    working_folder = os.path.join(foldername,subfolder)
                    source_files = os.listdir(working_folder)
                    images = [s for s in source_files if s.endswith('.png')]
                    if not images:
                        for file in source_files:
                            if os.path.isfile(os.path.join(working_folder, file)):
                                old_file = os.path.join(working_folder,file)
                                new_file = os.path.join(self.temp_scripts_path, foldername[self.base_path_length:], subfolder,file)
                                shutil.copyfile(old_file, new_file)
                    self.recursive_make(subfolder)
            for filename in filenames:
                file = os.path.join(foldername,filename)
                images = [s for s in os.listdir(foldername) if s.endswith('.png')]
                if ".py" in filename and ".sikuli" in foldername and images:
                    self.make_py_file(foldername[self.base_path_length:], filename)

    def make_py_file(self, existing_script_folder, py_file):
        #existing_script_folder = "check_keyboard_switching.sikuli"
        #make_sub_dir(existing_script_folder)
        #py_file = existing_script_folder[0:-7]+".py"
        old_py_file=os.path.join(self.old_scripts_path,existing_script_folder,py_file)
        old_file = open(old_py_file,"r")
        print("making: "+old_py_file)
        ### temp_py_file contains prompts
        temp_py_file = os.path.join(self.temp_scripts_path,existing_script_folder,py_file)
        temp_file = open(temp_py_file,"w+")
        #write boilerplate as base temp_file
        if os.path.dirname(existing_script_folder) != "":
            name = "__file__"
        else:
            name = "sys.argv[0]"
            temp_file.write("import sys\n")
        temp_file.write("from image_updater import ImageUpdater\n")
        temp_file.write('my_image_updater = ImageUpdater('+name+')\n')
        temp_file.write('print("#######################\\nworking in :"+'+name+'+"\\n#######################")\n')
        # get all images from folder
        images = [s for s in os.listdir(os.path.join(self.old_scripts_path,existing_script_folder)) if s.endswith('.png')  or s.endswith('.jpeg') or s.endswith('.jpg')]
        #parse file
        line_num = 1
        for line in old_file:
                start_whites = line[:len(line)-len(line.lstrip())] #preserve whitespace
                if (".png" in line) or (".jpeg" in line) or (".jpg" in line):
                    for image in images:
                        m = re.findall(image, line)
                        if any(image in s for s in m):
                            # check if file already captured if so move on
                            line_data = "<"+str(line_num)+"> "+(line.rstrip("\r\n")).lstrip()
                            my_reg = 'similar\(([0-1]*\.[0-9]+)'
                            s = re.findall(my_reg, line)
                            if len(s) == 0:
                                my_similarity = '"default"'
                                #print("no similarity")
                            elif len(s) == 1:
                                #print("similarity is: "+s[0])
                                my_similarity = s[0]
                            else:
                                pass
                                #print("----More than one similarity on a line----")
                            temp_file.write(start_whites+'my_image_updater.prompt("'+image+'", '+str(my_similarity)+', \"\"\"'+line_data+'\"\"\")\n')
                temp_file.write(line)
                line_num +=1
        old_file.close()
        temp_file.close()
        # TODO Move All files to new location
        # new_py_file uses new images, but is a pretty close copy of the original py
        # new_py_file = make_file(self.old_scripts_path+py_file)



    def prompt(self, my_image, my_sim, line_data):
        self.make_hotkeys()
        print(line_data)
        self.image_name = my_image
        self.line_text = line_data
        self.similarity = my_sim
        #get path to folder
        self.image_path = os.path.join(self.old_scripts_path,self.mwd[self.temp_path_length:],my_image)
        new_image_path = os.path.join(self.temp_scripts_path,self.mwd[self.temp_path_length:],my_image)
        if os.path.exists(new_image_path):
            self.capture_path = new_image_path
            wait(1)
            type(Key.F5, KeyModifier.SHIFT+KeyModifier.CTRL) #move_on
        else:
            #if self.show_prompt:
            #    type(Key.F1, KeyModifier.SHIFT+KeyModifier.CTRL) #show_instructions
            type(Key.F2, KeyModifier.SHIFT+KeyModifier.CTRL) #show_image
            self.my_event.clear()
            self.my_event.wait() #wait for set in move_on

    def show_instructions(self, event):
        print("show instructions")
        popup("An image needs to be captured corresponding to the following image:\n \
                    Press CTRL+SHIFT+F1 to show these instructions again\n \
                    Press CTRL+SHIFT+F2 to show the image again\n \
                    Press CTRL+SHIFT+F3 to capture an image\n \
                         or Press CTRL+SHIFT+F6 to use exisitng image\n \
                    Press CTRL+SHIFT+F4 to show the image you chose\n \
                    Press CTRL+SHIFT+F7 to test the image you chose\n \
                    Press CTRL+SHIFT+F5 to move on \n \
                       \n \
                    This is the line that will be executed:\n \
                    "+self.line_text, "Capture an Image" )
        self.show_prompt = False

    def show_image(self, event):
        print("show_image")
        if self.showing_PNG:
            popup("Close all popups. The program cannot proceed unless they are closed.", "show image ERROR")
            return
        #show image
        self.show_PNG(self.image_path, "<- This is the original image. The image will be searched for after you press OK.\n"+self.line_text)
        self.showing_PNG = False
        wait(3)
        #test if existing image works
        found_it = self.test_find(None)
        if found_it:
            type(Key.F6, KeyModifier.SHIFT+KeyModifier.CTRL) #use existing

    #TODO follow mouse (onMouseMove) with highlight box
    # import struct #for dimensions function
    #L=Env.getMouseLocation()
    #with open(self.image_path, 'rb') as f:
    #    data = f.read()
    #    w, h = struct.unpack('>LL', data[16:24])
    #    width = int(w)
    #    height = int(h)
    #Region(L.getX()-width/2, L.getY()-height/2, width,height).highlight(1)

    def capture_new_image(self, event):
        print("capture an image")
        if self.showing_PNG:
            popup("Close all popups. The program cannot proceed unless they are closed.", "capturing ERROR")
            return
        temp_image=capture()
        if temp_image != None:
            self.capture_path = temp_image
            #copy file to working directory
            shutil.copyfile(temp_image, os.path.join(self.mwd, self.image_name))


    def show_capture(self, event):
        if self.showing_PNG:
            popup("Close all popups. The program cannot proceed unless they are closed.", "show capture ERROR")
            return
        print("show the capture")
        self.show_PNG(self.capture_path, "<- This is the captured image.")
        self.showing_PNG = False

    def move_on(self, event):
        print("move on")
        if self.showing_PNG:
            popup("Close all popups. The program cannot proceed unless they are closed.", "move on ERROR")
            return
        if self.capture_path == "-":
            popup("Nothing has been captured yet", "ERROR")
        else:
            self.my_event.set()
            self.capture_path ="-"
            self.image_name = "-"
            self.image_path = "-"
            self.line_text = "-"
            self.remove_hotkeys()

    def use_existing(self, event):
        print("use_existing")
        self.capture_path = self.image_path
        shutil.copyfile(self.image_path, os.path.join(self.mwd, self.image_name))
        type(Key.F5, KeyModifier.SHIFT+KeyModifier.CTRL) #move_on

    def test_find(self, event):
        print("test_finding")
        #copy image to working directory
        if self.capture_path == "-":
            print(self.image_path)
            test_image_path = self.image_path #self.make_temp_image_for_search(self.image_path)
        else:
            print(self.capture_path)
            test_image_path = self.capture_path #self.make_temp_image_for_search(self.capture_path)
        result = False
        try:
            if self.similarity == "default":
                found = find(test_image_path)
            else:
                found = find(test_image_path).similar(self.similarity)
            print("trying to find image")
            result = True
            print("found it!")
            if self.myOS == OS.LINUX:
                pass
            elif self.myOS == OS.WINDOWS:
                found.highlight(2)
            else:
                popup("unsupported OS","ERROR")
        except:
            popup("Image was not found\n"+self.image_path, "ERROR")
            result =  False
        print("done looking")
        return result

    def make_temp_image_for_search(self, passed_image_name):
        # TODO Test to see if this function is needed for helper files
        print("making temp image for seach")
        print("src: "+passed_image_name)
        temp_image_path = os.path.join(os.path.dirname(self.test), self.image_name)
        print("dst: "+temp_image_path)
        shutil.copyfile(passed_image_name, temp_image_path)
        wait(1)
        return temp_image_path

    def show_PNG(self,img,message):
        self.showing_PNG = True
        icon = ImageIcon(img)
        JOptionPane.showMessageDialog(None, message, "About", JOptionPane.INFORMATION_MESSAGE, icon);

    def show_PNG2(self,img,message):
        #TODO Remove. Keeping in case secondary wait is needed. Currently unused.
        self.frame = JFrame("Here is the image", defaultCloseOperation = WindowConstants.EXIT_ON_CLOSE)
        self.frame.setResizable(False)
        panel = JPanel()
        label = JLabel()
        button = JButton("OK",actionPerformed=self.clickOK)
        label.setBorder(BorderFactory.createLineBorder(Color.red, 2))
        icon = ImageIcon(img)
        label.setIcon(icon)
        label2 = JLabel()
        label2.setText(message)
        panel.add(label)
        panel.add(label2)
        panel.add(button)
        self.frame.getContentPane().add(panel)
        self.frame.pack()
        self.frame.setVisible(True)
        self.my_event2.clear()
        self.my_event2.wait()

    def clickOK(self, event):
        # TODO Remove. Used by show_PNG2.
        self.frame.setVisible(False)
        self.frame.dispose()
        self.my_event2.set()

    def make_hotkeys(self):
        Env.addHotkey(Key.F1, KeyModifier.SHIFT+KeyModifier.CTRL, self.show_instructions)
        Env.addHotkey(Key.F2, KeyModifier.SHIFT+KeyModifier.CTRL, self.show_image)
        Env.addHotkey(Key.F3, KeyModifier.SHIFT+KeyModifier.CTRL, self.capture_new_image)
        Env.addHotkey(Key.F4, KeyModifier.SHIFT+KeyModifier.CTRL, self.show_capture)
        Env.addHotkey(Key.F5, KeyModifier.SHIFT+KeyModifier.CTRL, self.move_on)
        Env.addHotkey(Key.F6, KeyModifier.SHIFT+KeyModifier.CTRL, self.use_existing)
        Env.addHotkey(Key.F7, KeyModifier.SHIFT+KeyModifier.CTRL, self.test_find)

    def remove_hotkeys(self):
        Env.removeHotkey(Key.F1, KeyModifier.SHIFT+KeyModifier.CTRL)
        Env.removeHotkey(Key.F2, KeyModifier.SHIFT+KeyModifier.CTRL)
        Env.removeHotkey(Key.F3, KeyModifier.SHIFT+KeyModifier.CTRL)
        Env.removeHotkey(Key.F4, KeyModifier.SHIFT+KeyModifier.CTRL)
        Env.removeHotkey(Key.F5, KeyModifier.SHIFT+KeyModifier.CTRL)
        Env.removeHotkey(Key.F6, KeyModifier.SHIFT+KeyModifier.CTRL)
        Env.removeHotkey(Key.F7, KeyModifier.SHIFT+KeyModifier.CTRL)

    def check_images(self):
        #check if all images in old folder are in new folder
        old_images = [s for s in os.listdir(os.path.join(self.old_scripts_path,self.pwd)) if s.endswith('.png')  or s.endswith('.jpeg') or s.endswith('.jpg')]
        temp_images = [s for s in os.listdir(os.path.join(self.temp_scripts_path,self.pwd)) if s.endswith('.png')  or s.endswith('.jpeg') or s.endswith('.jpg')]
        #TODO Copy old non-captured files.

#recursive loop for sikuli folders
if __name__ == "__main__":
    from image_updater import ImageUpdater
    my_image_updater = ImageUpdater("test")
    my_image_updater.recursive_make() #This copies the files and folders to the temporary folder.

    # Make image_updater directory in temp_scripts_path
    my_image_updater.make_sub_dir("image_updater.sikuli")
    my_new_path = my_image_updater.temp_scripts_path+"image_updater.sikuli"
    # Copy all files from image_updater to new directory
    source_files = os.listdir(my_image_updater.my_path)
    for file in source_files:
        if os.path.isfile(os.path.join(my_image_updater.my_path, file)):
            old_file = os.path.join(my_image_updater.my_path,file)
            new_file = os.path.join(my_new_path,file)
            shutil.copyfile(old_file, new_file)

    # Run prompt scripts
    # Copy old scripts over prompt scripts
    # Test new script

    ### NOTES ###
    #make hash of image paths (old_name, old_image, new_image)
    #keep track of last known location and try it

