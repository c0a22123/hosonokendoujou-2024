
//*base.html
document.addEventListener("DOMContentLoaded", function() {
  const popupButton = document.getElementById('popupButton');
  const popupWindow = document.getElementById('popupWindow');

  // メニュータブを開閉するためのイベントリスナー
  popupButton.addEventListener('click', function() {
      if (popupWindow.style.display === 'block') {
          popupWindow.style.display = 'none';
      } else {
          popupWindow.style.display = 'block';
      }
  });

  // メニュー外をクリックしたら閉じる
  document.addEventListener('click', function(event) {
      if (!popupButton.contains(event.target) && !popupWindow.contains(event.target)) {
          popupWindow.style.display = 'none';
      }
  });
});
