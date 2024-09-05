// メニューの開閉を管理
const popupButton = document.getElementById('popupButton');
const popupWindow = document.getElementById('popupWindow');

// メニューボタンをクリックしたらメニューを開閉
popupButton.addEventListener("click", function() {
  toggleDropdown(); // メニューの開閉を切り替える
});

function toggleDropdown() {
  if (popupWindow.style.display === "block") {
    popupWindow.style.display = "none"; // メニューを閉じる
  } else {
    popupWindow.style.display = "block"; // メニューを開く
  }
}