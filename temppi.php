<?php
$ip = implode('', file ('/var/www/html/saveip/ip.txt'));

function get_content($url)
{
    $ch = curl_init();

    curl_setopt ($ch, CURLOPT_URL, $url);
    curl_setopt ($ch, CURLOPT_HEADER, 0);

    ob_start();

    curl_exec ($ch);
    curl_close ($ch);
    $string = ob_get_contents();

    ob_end_clean();
    
    return $string;     
}

$temperature = get_content('http://'.$ip.':9898/cgi-bin/t.py');

header('Content-type: text/html');
header('Access-Control-Allow-Origin: *');
echo $temperature;

?>