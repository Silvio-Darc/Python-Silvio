<!DOCTYPE html>
<html lang="pt">
<head>
    <title>Top Animes</title>
</head>
<body>


<?php

$aLimit = isset($_POST['formLimit']) ? $_POST['formLimit'] : 3;
$aOrderBy = isset($_POST['formOrderBy']) ? $_POST['formOrderBy'] : '';

echo '
<form method=POST action=top-animes.php>
    <label>
        Top
        <input name=formLimit value=' .($aLimit).'>
    </label>
    <label>
        Ordenados por
        <select name=formOrderBy>
            <option value="" '.($aOrderBy=='' ? 'selected="selected"' : '').' >Nada</option>
            <option value="favorites" '.($aOrderBy=='favorites' ? 'selected="selected"' : '').' >Favoritos</option>
            <option value="popularity" '.($aOrderBy=='popularity' ? 'selected="selected"' : '').' >Popularidade</option>
        </select>
    </label>
    <input type=submit value=Ordenar>
</form>
';

$url = "https://api.jikan.moe/v4/anime?order_by=$aOrderBy&limit=$aLimit";

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
curl_close($ch);

$json_decoded = json_decode($response);

for ($i = 0; $i < count($json_decoded->data); ++$i) {
    $anime = $json_decoded->data[$i];
    echo "<h2>$anime->title</h2>";
    $from = $anime->aired->prop->from;
    $to = $anime->aired->prop->to;
    echo "<p>";
    echo "De $from->day, $from->month, $from->year";
    echo " ate $to->day, $to->month, $to->year";
    echo "</p>";
    echo "<b><label>Sinopsis</label></b><p>$anime->synopsis</p>";
    $image_url = $anime->images->jpg->image_url;
    echo "<img src=$image_url alt=$anime->title>";
}

?>
</body>
</html>