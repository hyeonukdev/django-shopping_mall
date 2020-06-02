var voices = [];

function setVoiceList() {
    voices = window.speechSynthesis.getVoices();
}
setVoiceList();
if (window.speechSynthesis.onvoiceschanged !== undefined) {
    window.speechSynthesis.onvoiceschanged = setVoiceList;
}

function speech(txt) {
    if (!window.speechSynthesis) {
        alert("지원불가");
        return;
    }
    var lang = 'ko-KR';
    var utterThis = new SpeechSynthesisUtterance(txt);
    utterThis.onend = function (event) {
        console.log('end');
    };
    utterThis.onerror = function (event) {
        console.log('error', event);
    };
    var voiceFound = false;
    for (var i = 0; i < voices.length; i++) {
        if (voices[i].lang.indexOf(lang) >= 0 || voices[i].lang.indexOf(lang.replace('-', '_')) >= 0) {
            utterThis.voice = voices[i];
            voiceFound = true;
        }
    }
    if (!voiceFound) {
        alert('voice not found');
        return;
    }
    utterThis.lang = lang;
    utterThis.pitch = 1;
    utterThis.rate = 1;
    window.speechSynthesis.speak(utterThis);
}
document.addEventListener("keydown", function (e) {
    if (e.keyCode == 83) {
        alert('s 입력')
        var tts = e.target;
        speech(tts.value);
    }

});