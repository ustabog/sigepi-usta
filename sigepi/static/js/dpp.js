function mostrar()
{
  $("#btn-menu").click(
    function ()
    {
      $("#wrapper").toggleClass("activo");
      alert("Me haz dado un click");
    }
  );
}
