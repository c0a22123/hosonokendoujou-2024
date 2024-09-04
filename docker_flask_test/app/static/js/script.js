const popupButton = document.getElementById('popupButton');
const popupWindow = document.getElementById('popupWindow');
const closeButton = document.querySelector('.close');

// ボタンがクリックされたときにポップアップを表示
popupButton.addEventListener('click', function() {
  popupWindow.style.display = 'block';
});

// 閉じるボタンがクリックされたときにポップアップを非表示
closeButton.addEventListener('click', function() {
  popupWindow.style.display = 'none';
});

// ポップアップ外をクリックしたときにポップアップを非表示
window.addEventListener('click', function(event) {
  if (event.target == popupWindow) {
    popupWindow.style.display = 'none';
  }
});