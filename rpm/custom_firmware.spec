Name:           custom_firmware
Version:        0.1
Release:        0
License:        MIT
Summary:        images /vendor/bt_firmware, /vendor/dsp and /vendor/firmware_mnt
AutoReq: 	no

%description
This packages provides custom firmware images.

%install
mkdir -p $RPM_BUILD_ROOT/custom_firmware/
cp $ANDROID_ROOT/hybris/mw/custom_firmware/binaries/bluetooth.img $RPM_BUILD_ROOT/custom_firmware/bluetooth.img
cp $ANDROID_ROOT/hybris/mw/custom_firmware/binaries/dsp.img $RPM_BUILD_ROOT/custom_firmware/dsp.img
cp $ANDROID_ROOT/hybris/mw/custom_firmware/binaries/modem.img $RPM_BUILD_ROOT/custom_firmware/modem.img

%files
/custom_firmware/bluetooth.img
/custom_firmware/dsp.img
/custom_firmware/modem.img

%changelog
# Initial version

