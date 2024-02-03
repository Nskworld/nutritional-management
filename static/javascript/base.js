// タッチ開始位置を記録する変数
let touchStartX = 0;
let touchEndX = 0;

function handleTouchStart(event) {
    touchStartX = event.touches[0].clientX;
}

function handleTouchMove(event) {
    touchEndX = event.touches[0].clientX;
}

function handleTouchEnd() {
    // 左にスワイプした場合
    if (touchStartX > touchEndX + 50) { // スワイプ距離を50pxとする
        toggleSideMenu(); // サイドメニューの表示切り替え
    }
}

// サイドメニューの表示切り替え関数（前に作成したもの）
function toggleSideMenu() {
    var sideMenu = document.getElementById('side-menu');
    if (sideMenu.style.left === '0px') {
        sideMenu.style.left = '-40%'; // サイドメニューを非表示にする
    } else {
        sideMenu.style.left = '0px'; // サイドメニューを表示する
    }
}

// イベントリスナーをサイドメニューに追加
document.getElementById('side-menu').addEventListener('touchstart', handleTouchStart, false);
document.getElementById('side-menu').addEventListener('touchmove', handleTouchMove, false);
document.getElementById('side-menu').addEventListener('touchend', handleTouchEnd, false);
