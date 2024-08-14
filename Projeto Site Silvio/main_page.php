<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <title>Top Animes Silvio</title>
</head>
<body style="background-color: darkslateblue;color: aliceblue;font-family:'Roboto Light',sans-serif">
<?php
$quantity = 1;
$criteria = "Mais popular"
?>
<h1>Top Animes no MAL</h1>
<h4>Escolha a quantidade e o critério:</h4>

<form action="main_page.php" method="get">
    <label for="criteria">Critérios</label>
    <select id="criteria" name="criteria">
        <option value="Mais popular">Mais Popular</option>
        <option value="Mais assistido">Mais assistido</option>
        <option value="Mais recente">Mais recente</option>
        <option value="Menos popular">Menos popular</option>
        <option value="Menos assistido">Menos assistido</option>
        <option value="Menos recente">Menos recente</option>
    </select>
    <label for="quantity">Quantidade:</label>
    <input type="number" id="quantity" name="quantity" min="1" required value="3">
    <input type="submit" value="Pesquisar">
</form>
<?php
$quantity = isset($_GET["quantity"]) ? $_GET["quantity"] : 3;
$criteria = isset($_GET["criteria"]) ? $_GET["criteria"] : "Mais Popular";
echo "Quantidade: $quantity<br>";
echo "Critério: $criteria";
?>


</body>
</html>