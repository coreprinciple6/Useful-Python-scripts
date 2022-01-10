### For installing ubuntu
1.	Allocate 100 gb  (92gb for main and 8gb for swap partition) from windows disc manager
2.	Use rufus to create a bootable ubuntu usb drive.  I had to use UEFI
3.	Plug in the pendrive and restart
4.	Follow the steps as required
5.	For nvidia , **purge** everything and then open terminal to run the following command:
    
    ```
    a.	Sudo apt-get nvidia prime
    b.	Sudo apt autoinstall
    c.	 nvidia-smi
    ```
6.	This helped install ubuntu:  https://www.tecmint.com/install-ubuntu-alongside-with-windows-dual-boot/
7.	This too: https://www.youtube.com/watch?v=-iSAyiicyQY

### For uninstalling ubuntu

1.	Login to windows again and delete the ubuntu partition
2.	If u restart and u see that u blacked out just type exit in GRUB interface to login to windows again
3.	Follow this instruction to delete  grub bootloader from windows: https://www.binaryera.com/2020/08/RemoveGrubFromWindow10.html?m=1&fbclid=IwAR10qOQcHN7MIyAVJcaEPbc0fmi_epkNGqZHObIEhEtyfbjIvydBQ1i2Slw
4.	Follow this to create a windows recovery usb drive: https://www.howtogeek.com/131907/how-to-create-and-use-a-recovery-drive-or-system-repair-disc-in-windows-8/?fbclid=IwAR3MlD1MnW1kq-dfwn3trnNTPOZXuYbecRl3bk4Nj6Sffnhp0RJQObGG32o
5.	This only partly helped in uninstalling ubuntu: https://askubuntu.com/questions/1123089/uninstall-ubuntu-dual-boot?fbclid=IwAR0ZdtC8seOvFoeuNi7TVUxBXsP7XcRWMEkp1eJw0ofH9ejiBZcPxGY51O0
6.	This helped delete partition in windows: https://www.thewindowsclub.com/merge-or-delete-an-oem-partition-in-windows?fbclid=IwAR2ttij8j8AxZAjfrvBYEIQGOhqCJIW_rmGp6fmZG9mzTsJhyT388J3lIBg
