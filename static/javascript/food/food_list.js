document.addEventListener('DOMContentLoaded', (event) => {
    const listItems = document.querySelectorAll('.list-item');

    listItems.forEach(item => {
        // Hammer.jsなどのライブラリを使ってスワイプイベントを検出できます
        const hammertime = new Hammer(item);
        hammertime.on('swipeleft', function(ev) {
            item.classList.add('open'); // アクションを表示
        });
        hammertime.on('swiperight', function(ev) {
            item.classList.remove('open'); // アクションを隠す
        });
    });
});

function editFood(id) {
    // 編集機能の実装
}

function deleteFood(id) {
    // 削除機能の実装
}
