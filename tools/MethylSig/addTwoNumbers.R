addTwoNumbers <-
function(
        number1=GalaxyNumericParam(required=TRUE),
        number2=GalaxyNumericParam(required=TRUE),
        sum=GalaxyOutput("sum", "txt"))
{
    cat(number1 + number2, file=sum)
}
