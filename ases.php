<?php 
 
$param1 = floatval($_POST['academic']/10);
$param2 = intval($_POST['sports']);
$param3 = intval($_POST['debdisc']);
$param4 = intval($_POST['dancedram']);
$param5 = intval($_POST['tpp']);
$param6 = intval($_POST['wexp']);
$command = "python /Users/Rahul/Desktop/LBS/ases.py";
$command .= " $param1 $param2 $param3 $param4 $param5 $param6 2>&1";
 
header('Content-Type: text/html; charset=utf-8');
echo '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />';

echo "<link type='text/css' rel='stylesheet' href='csstable.css' />";
echo "<link type='text/css' rel='stylesheet' href='csstable1.css' />";
$pid = popen( $command,"r");
 
echo "<body><pre>";
while( !feof( $pid ) )
{
 echo fread($pid, 256);
 flush();
 ob_flush();
// echo "<script>window.scrollTo(0,99999);</script>";
 usleep(100000);
}
pclose($pid);
 
echo "</pre><script>window.scrollTo(0,99999);</script>";
?>