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
cp src/binaries/bluetooth.img $RPM_BUILD_ROOT/custom_firmware/bluetooth.img
cp src/binaries/dsp.img $RPM_BUILD_ROOT/custom_firmware/dsp.img
cp src/binaries/modem.img $RPM_BUILD_ROOT/custom_firmware/modem.img
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system/
cp src/usr/lib/systemd/system/vendor-bt_firmware.mount $RPM_BUILD_ROOT/usr/lib/systemd/system/vendor-bt_firmware.mount
cp src/usr/lib/systemd/system/vendor-dsp.mount $RPM_BUILD_ROOT/usr/lib/systemd/system/vendor-dsp.mount
cp src/usr/lib/systemd/system/vendor-firmware_mnt.mount $RPM_BUILD_ROOT/usr/lib/systemd/system/vendor-firmware_mnt.mount

%files
/custom_firmware/bluetooth.img
/custom_firmware/dsp.img
/custom_firmware/modem.img
/usr/lib/systemd/system/vendor-bt_firmware.mount
ln -s /usr/lib/systemd/system/vendor-bt_firmware.mount /usr/lib/systemd/system/local-fs.target.wants/vendor-bt_firmware.mount
/usr/lib/systemd/system/vendor-dsp.mount
ln -s /usr/lib/systemd/system/vendor-dsp.mount /usr/lib/systemd/system/local-fs.target.wants/vendor-dsp.mount
/usr/lib/systemd/system/vendor-firmware_mnt.mount
ln -s /usr/lib/systemd/system/vendor-firmware_mnt.mount /usr/lib/systemd/system/local-fs.target.wants/vendor-firmware_mnt.mount

%changelog
# Initial version

