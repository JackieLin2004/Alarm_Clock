function setAlarm() {
    // 获取闹钟时间
    const alarmTime = document.getElementById("alarm-time").value;
    if (!alarmTime) {
        alert("请选择闹钟时间！");
        return;
    }

    // 计算闹钟时间距离当前时间的毫秒数
    const now = new Date();
    const [hour, minute] = alarmTime.split(":");
    const alarm = new Date(now.getFullYear(), now.getMonth(), now.getDate(), hour, minute);
    const timeDiff = alarm - now;


    // 设置闹钟
    if (timeDiff > 0) {
        // setTimeout(() => alert("时间到了！"), timeDiff);
        setTimeout(() => {
            document.getElementById('alarm-clock').play();
        }, timeDiff);
        alert("闹钟设置成功！");
    } else {
        alert("请选择未来的时间！");
    }
}

function closeAlarm() {
    let sound = document.getElementById('alarm-clock');
    sound.pause();
    sound.load();
}