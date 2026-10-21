> [!NOTE]
> - Mức độ: Dễ 
> - Loại: Forensics 
> - Url: [Illumination](https://app.hackthebox.com/challenges/Illumination)
> - Tình huống: Một lập trình viên cấp cơ sở vừa chuyển sang sử dụng một nền tảng quản lý mã nguồn mới. Bạn có thể tìm thấy mã thông báo (token) bí mật đó không?

> Giải nén tệp zip thu được thư mục mã nguồn được quản lý bởi git vẫn còn thư mục .git 

```
└─$ ls -al
total 8
drwxrwxr-x 1 kalilinux kalilinux   42 May 30  2019 .
drwxr-xr-x 1 kalilinux kalilinux  110 Oct 21 04:00 ..
-rw-rw-r-- 1 kalilinux kalilinux 2635 May 30  2019 bot.js
-rw-rw-r-- 1 kalilinux kalilinux  199 May 30  2019 config.json
drwxrwxr-x 1 kalilinux kalilinux  146 May 30  2019 .git
```

> Chương trình `bot.js` 
> - Discord phát sự kiện tin nhắn.
> - Bot kiểm tra người gửi có phải bot hay không.
> - Bot kiểm tra tin nhắn có bắt đầu bằng ! không.
> - Bot tách thành tên lệnh light.rgb và ba tham số RGB.
> - switch chọn nhánh light.rgb.
> - node-hue-api gửi yêu cầu đổi màu và bật đèn.
> - Bot tạo embed màu đỏ và gửi vào kênh Discord.
> - Khi API trả về thành công, kết quả được in ra console.


```javascript 
//Discord.JS
const Discord = require("discord.js");
const client = new Discord.Client();
const fs = require("fs");
var config = JSON.parse(fs.readFileSync("./config.json"));


//Node-Hue-API
var hue = require("node-hue-api"),
	HueApi = hue.HueApi,
	lightState = hue.lightState;

//Display command results in console
var displayResult = function(result) {

	console.log(JSON.stringify(result, null, 2));
	
};

//Function taken from campushippo.com
var rgbToHex = function (rgb) { 

  var hex = Number(rgb).toString(16);
  if (hex.length < 2) {

       hex = "0" + hex;
  }

  return hex;
};

//Function taken from campushippo.com
var fullColorHex = function(r,g,b) {   
  var header = "0x"
  var red = rgbToHex(r);
  var green = rgbToHex(g);
  var blue = rgbToHex(b);
  return header+red+green+blue;
};

//Declarations
var host = config.host,
	username = config.username,
	api = new HueApi(host, username),
	state = lightState.create(),
	prefix = config.prefix,
	lightNum = config.lightNum;

//Bot code
client.on("ready", () => {
	console.log(`Logged in as ${client.user.tag}!`);
});

client.on("message", message => {
	if (message.author.bot) return; //Ignore bot messages
	if (message.content.indexOf(prefix) !== 0) return; //Ensure prefix is at the beginning

	const args = message.content.slice(prefix.length).trim().split(/ +/g); //Split command into arguments
	const command = args.shift().toLowerCase(); 

	switch (command) {

		case "light.off" : //Turn light off
			api.setLightState(lightNum, state.off())
		       .then(displayResult)
		       .done();
			message.channel.send("Light Off!");
			break;

		case "light.on" : //Turn light on
			api.setLightState(lightNum, state.on())
			   .then(displayResult)
			   .done();
			message.channel.send("Light On!");
			break;

		case "light.rgb" : //Change light colour
			let r = args[0];
			let g = args[1];
			let b = args[2];
			api.setLightState(lightNum, state.on().rgb(r, g, b))
			   .then(displayResult)
			   .done();
			const embed = new Discord.RichEmbed()
				.setTitle('Light Colour Change')
				.setColor(fullColorHex(r, g, b))
				.setDescription(`Red Value: ${r}. Green Value: ${g}. Blue Value: ${b}`);
			message.channel.send(embed);
			break;

		case "light.switch" : //Switch to different light
			let num = args[0];
			lightNum = num;
			//fs.writeFile("./config.json", JSON.stringify(config))
			message.channel.send(`Light Number switched to ${lightNum}`);
	}
});

client.login(Buffer.from(config.token, 'base64').toString('ascii')) //Login with secret token
```

> - File 'config.json' chứa token và các thông tin thiết lập khác nhưng token đã bị xóa 

```json
{

	"token": "Replace me with token when in use! Security Risk!",
	"prefix": "~",
	"lightNum": "1337",
	"username": "UmVkIEhlcnJpbmcsIHJlYWQgdGhlIEpTIGNhcmVmdWxseQ==",
	"host": "127.0.0.1"

}
```

> - Username là 1 chuỗi base64 nhwung khi giải mã thì đây là dữ liệu gây nhiễu 
```
└─$ echo UmVkIEhlcnJpbmcsIHJlYWQgdGhlIEpTIGNhcmVmdWxseQ== | base64 -d
Red Herring, read the JS carefully  
```

> - Xem lịch sử commit của repo đọc các comment có thông tin về việc xóa token khỏi file config.json 

```
└─$ git log      
commit edc5aabf933f6bb161ceca6cf7d0d2160ce333ec (HEAD -> master)
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 14:16:43 2019 +0100

    Added some whitespace for readability!

commit 47241a47f62ada864ec74bd6dedc4d33f4374699
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 12:00:54 2019 +0100

    Thanks to contributors, I removed the unique token as it was a security risk. Thanks for reporting responsibly!

commit ddc606f8fa05c363ea4de20f31834e97dd527381
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 09:14:04 2019 +0100

    Added some more comments for the lovely contributors! Thanks for helping out!

commit 335d6cfe3cdc25b89cae81c50ffb957b86bf5a4a
Author: SherlockSec <dan@lights.htb>
Date:   Thu May 30 22:16:02 2019 +0100

    Moving to Git, first time using it. First Commit!
```

> - Xem commit xóa token hoặc các commit trước đó sẽ lấy được token `SFRCe3YzcnNpMG5fYzBudHIwbF9hbV9JX3JpZ2h0P30=`

```
└─$ git show 47241a47f62ada864ec74bd6dedc4d33f4374699
commit 47241a47f62ada864ec74bd6dedc4d33f4374699
Author: SherlockSec <dan@lights.htb>
Date:   Fri May 31 12:00:54 2019 +0100

    Thanks to contributors, I removed the unique token as it was a security risk. Thanks for reporting responsibly!

diff --git a/config.json b/config.json
index 316dc21..6735aa6 100644
--- a/config.json
+++ b/config.json
@@ -1,6 +1,6 @@
 {
 
-       "token": "SFRCe3YzcnNpMG5fYzBudHIwbF9hbV9JX3JpZ2h0P30=",
+       "token": "Replace me with token when in use! Security Risk!",
        "prefix": "~",
        "lightNum": "1337",
        "username": "UmVkIEhlcnJpbmcsIHJlYWQgdGhlIEpTIGNhcmVmdWxseQ==",

```

> - Token là chuỗi mã hóa base64 giải mã thu được flag 

```
└─$ echo SFRCe3YzcnNpMG5fYzBudHIwbF9hbV9JX3JpZ2h0P30= | base64 -d    
HTB{v3rsi0n_c0ntr0l_am_I_right?} 
```