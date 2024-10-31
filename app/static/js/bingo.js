// static/js/bingo.js

let qrCodeReader = null;

// カメラを起動してQRコードを読み取る関数
function startCamera() {
    // すでにQRコードリーダーが存在する場合、停止して破棄
    if (qrCodeReader) {
        qrCodeReader.stop().then(() => {
            document.getElementById('qr-reader').innerHTML = ''; // リーダーの内容をクリア
            initializeQrReader(); // 新たなインスタンスを生成してカメラを再起動
        }).catch(err => console.error("QRコードリーダーの停止エラー:", err));
    } else {
        initializeQrReader();
    }
}

// QRコードリーダーのインスタンスを初期化し、カメラを起動する
function initializeQrReader() {
    qrCodeReader = new Html5Qrcode("qr-reader");
    qrCodeReader.start(
        { facingMode: "environment" },
        { fps: 10, qrbox: 250 },
        handleQrCodeSuccess,
        handleQrCodeError
    ).catch(err => console.error("QRコードリーダーの起動エラー:", err));
}

// QRコードが正常に読み取られたときの処理
function handleQrCodeSuccess(qrCodeMessage) {
    console.log(`QRコードが読み取られました: ${qrCodeMessage}`);
    
    qrCodeReader.stop().then(() => {
        document.getElementById('qr-reader').style.display = 'none';
        document.getElementById('qr-reader').innerHTML = ''; // QRリーダーの内容をクリア
        fetch(`/stamp/${qrCodeMessage}`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const cellId = data.cell_id - 1;
                    updateCell(cellId);
                    showOverlay(data.spot_name, data.spot_trivia);
                } else {
                    alert('無効なQRコードです');
                }
            })
            .catch(error => console.error('エラー:', error));
    }).catch(err => console.error("カメラ停止エラー:", err));
}

// QRコード読み取りエラー時の処理
function handleQrCodeError(errorMessage) {
    console.warn(`QRコード読み取りエラー: ${errorMessage}`);
}

// ビンゴセルを更新する関数
function updateCell(cellId) {
    const cell = document.getElementById(`cell-${cellId}`);
    cell.innerHTML = `<img src="/static/images/stamp/tamabingo_stamp.png" alt="スタンプ ${cellId + 1}">`;
    cell.classList.add("checked");
}

// オーバーレイを表示する関数
function showOverlay(spotName, trivia) {
    document.getElementById('spot-name').textContent = `${spotName} のスタンプが押されました！`;
    document.getElementById('spot-trivia').textContent = trivia;
    document.getElementById('overlay').style.display = 'flex';
}

// オーバーレイを閉じる関数
function closeOverlay() {
    document.getElementById('overlay').style.display = 'none';
    closeCamera();
}

// カメラを手動で閉じる関数
function closeCamera() {
    if (qrCodeReader) {
        qrCodeReader.stop().then(() => {
            document.getElementById('qr-reader').style.display = 'none';
            document.getElementById('qr-reader').innerHTML = ''; // QRリーダーの内容をクリア
            qrCodeReader = null; // インスタンスを破棄
        }).catch(err => console.error("カメラ停止エラー:", err));
    }
}

// 景品交換ボタンとポップアップの制御
function setupPrizeExchange() {
    document.getElementById('exchange-prize').addEventListener('click', () => {
        document.getElementById('exchange-popup').style.display = 'flex';
    });

    document.getElementById('confirm-exchange').addEventListener('click', () => {
        // サーバーへ景品交換のリクエストを送信
        fetch('/exchange_prize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('exchange-message').textContent = data.message;
                document.getElementById('exchange-prize').textContent = '景品は交換済みです';
                document.getElementById('exchange-prize').disabled = true;
            } else {
                alert(data.message);
            }
            setTimeout(() => {
                document.getElementById('exchange-popup').style.display = 'none';
            }, 1000);
        })
        .catch(error => console.error('交換エラー:', error));
    });

    document.getElementById('cancel-exchange').addEventListener('click', () => {
        document.getElementById('exchange-popup').style.display = 'none';
    });
}


// イベントリスナーを初期化
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('start-camera').addEventListener('click', startCamera);
    setupPrizeExchange();
});
