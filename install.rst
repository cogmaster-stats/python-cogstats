=======================================
Getting ready: installing the software
=======================================


.. topic:: **Content**
 
   This page will help you installing a virtual machine that
   includes all the softwares we will use during the next courses on the
   analysis of fMRI data.

.. warning::

   The installation is a bit tricky, please read the corresponding
   paragraph **before** trying anything, usually a computer doesn't work the
   way you suppose it would: it follows the tortuous mind of its
   programmer. If you fail to install the virtual machine, ask a friend
   to help you, if it doesn't work, please sit next to someone who made
   it for the next lecture: questions related to the installation will
   only be answered at the end of the lecture. By the way the downloads
   and installations might take quite a while, make sure you have some
   articles to read nearby and do it earlier than on the morning of the
   first course.

.. topic:: **Prerequisites**

  Make sure you know where a file that you download from the internet is
  saved on your computer. Usually, there is a default "Download" folder
  not that deep from your home directory (check the preferences of your
  favorite browser), for example:

    - On windows: C:\\User\\your_user_name\\Download\\
    - On mac: /Users/your_user_name/Downloads/
    - On some linux: /home/your_user_name/Download/

  If you are using a recent enough Mozilla Firefox browser, the general
  panel in the preferences allows you to select the option "always ask me
  where to save file", which is useful to download a file where you want
  it to be stored.


Installation
============

Sanity check
------------

Check that the Operating System currently running on your computer (the
so-called "host" OS, which is usually windows, macOS or linux) currently
running on your computer) appears in the following list:
https://www.virtualbox.org/manual/ch01.html#hostossupport If not, well,
too bad for you, please install one of the supported OS on a different
partition. 

Download the neurodebian virtual machine
----------------------------------------

Go the the website of the NeuroDebian repository http://neuro.debian.net/
and under "Get NeuroDebian", select the Operating System (the so-called
"host" OS, which is usually windows, macOS or linux) currently running on
your computer. Then select the nearest server and download the "Virtual
applicance image dile", which is a rather heavy file with a ".oda"
extension.

For those using windows, I suggest you try the Germany (Nikilaus Valentin
Haenel, Vogtland) server so you would get an .ova file and wouldn't have
to struggle to decompress the file.

If you are using a linux system, unless you know exacly what you are
doing and you'd rather install the various packages by yourself and won't
complain if you miss something during the lecture, I recommend that you
install the neurodebian virtual machine as well. You can pick either the
32bit or 64bit version from the MS Windows choice in the list. 

Download the VirtualBox installer
---------------------------------

From the website http://www.virtualbox.org/wiki/Downloads download the
last available "VirtualBox platform package" corresponding to your host
OS (the X stands for the version numbers, which changed twice this weak,
it doen't really matter):

- VirtualBox 4.X.X for Windows hosts if you are using Windows;
- VirtualBox 4.X.X for OS X hosts if you are using a Mac;
- and follow the link for the Linux hosts if you are using a linux, and
  proceed according to your distribution.


Install VirtualBox
------------------

**Read the installation instructions** related to your host OS 
https://www.virtualbox.org/manual/ch02.html

Go in the directory where the installer file is and then:

- on window, double click on the downloaded .exe file (on windows 7 and
  probably vista and 8, wait until the warning windows on darkened
  blackground appears, and click "yes"; It usually takes few seconds, so
  wait and don't click again and again on the installer). Then click on
  "Next" on the installer until you have to click on "install". You will be
  then see several pop up windows asking you to install drivers, select
  "install" each time.

- on macOS, double click on the VirtualBox-4.3.2-90405-OSX.dmg file and
  once the virtual disk content pops up, double click on the VirtualBox.pkg
  icon and then click on "continue" and "install" and enter your
  administrator password as prompted. When the Install is done, close the
  package installer and dismount ("eject") the virtual disk from your
  finder.

- on Ubuntu linux or debian-based distribution, run apt-get to install
  dkms and then dpkg to install VirtualBox. For other distributions I
  assume you know what to do.

Now, **before** you do anything, go read the instructions on the
neurodebian website: http://neuro.debian.net/vm.html#chap-vm Don't follow
the configuration instructions from the virtualbox website. Don't start
the VirtualBox and click everywhere, especially not on that shiny blue
sunny "New" button.

Configure the neurodebian virtual machine
-----------------------------------------

Follow the instructions from
http://neuro.debian.net/vm.html#chap-vm

1. No need to create a new machine, you already downloaded one, thus use
   "Import Appliance" from the file menu and sleect the NeuroDebian virtual
   appliance file in the folder where it was stored.

2. Wait while the NeuroDevian__disk1.vmdk is retrieved and installed

3. Once your wirtual machine appears in the left column, DON'T START IT:
   you have to configure it first using the "Settings" cog-like button. Yep,
   there's a good reason it's on the left of the start button.

4. first important thing to configure: the alount of RAM you are
   allocating to the wirtual machine. More is better, but try to keep some
   RAM for the host OS.

5. second important thing to configure: the shared folder: usually, a
   carefully named (i.e. no space, no accent, no weird character, mine is
   called "ndb") folder in your home directory.

Finally it is time to actually start using the virtual machine: click on
the "arrow" stat icon. You can see the different steps of a debian boot,
on text mode, before it switches to graphic environment if anything goes
wrong, i.e. it does get stuck in the boot process (I experiences a kernel
panic once). Just shut down the virutal machine, using the virtual
machine menu called "machine" and then "APIC Shutdown". Then right click
on the Virtual Machine in the left panel and remove it. Then proceed to
the virtual machine installation again.

Automatically, on the first boot, the NeuroDebian Setup Wizard starts and
welcomes you. Once again, you'd better do some configuration before
clicking on the "OK" button at the bottom of the Setup Wizard window that
just poped up. So Click on "Applications Menu" on the top left of the
screen, then "Settings", "Keyboard", the "Layout" tab, unselect the "Use
system defaults" option, select the "Keyboard model" if needed, and "Add"
a french layout, or any layout that matches yours (delete the other ones
to be sure), then close the window. You can test your keyboard on a
"Application Menu"->"Terminal Emulator". Unless you'd like to enter
the password neurodebian as it you had a qwerty keyboard (thus typing
"neurodebiqn with a French keyboard").

So, back to the NeuroDebian Setup Wizard.
First you will be asked to install some updates to your system, make sure your computer is connected to the internet, then carry on, and enter the password "neurodebian".
Once you have downloaded and installed the , click on the "Close" button and a new setup wizard window appears that will help you install some very useful additional packages. You can participate to the packages popularity survey if you want, then, select Python: Neuroimaging. If you want to look at the virtual machine video demo from within the virtual machine, you'd better select the Adobe Flash plugin as well.
This installation will take few minutes.

As the installation completes, the web browser will show you the NeuroDebian Virtual Machine Welcome page.
However the installation for our purpose still needs few steps: we will now install specific neuroimaging packages.
Go to the "Application menu" -> "NeuroDebian" -> "Medical Imaging", then select the following packages and install them one after the other:

- "dcm2nii"
- "FSLView"
- "FSL 4.1", this one is quite long, you can use that time to look at the
  video tutorial on the Neurodebian Virtual MAchine Welcome page.


Now you are ready.
You can shutdown the virtual machine using the little exit icone on the
right of the Application Menu on the to left of the wirtual machine
window. Then quit the virtualbox application.
On Monday, you will get another email telling you to get the last version
of the course files from the git repository. I'm still working on the
examples, it's not online yet.

