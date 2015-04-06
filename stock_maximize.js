function processData(input) {
    //Enter your code here
    input_list = input.split('\n');
    tests = parseInt(input_list[0]);
    for(var k = 1; k < input_list.length; k = k+2)
    {
            days = parseInt(input_list[k]);
            prices = input_list[k+1].split(' ').map(function(value){ return parseInt(value); });
            if(prices.length != days)
                return "Error";
            profit = 0;
            var maximum = [];
            maximum[prices.length-1] = prices[prices.length-1];
            for(var i = prices.length-2; i >= 0; --i)
                maximum[i] = Math.max(prices[i],maximum[i+1]);
            shares = 0;
            for(i = 0; i < prices.length; ++i)
                if(prices[i] < maximum[i])
                {
                    shares++;
                    profit = profit - prices[i];
                }
                else if(prices[i] == maximum[i])
                {
                    profit = profit + shares * maximum[i];
                    shares = 0;
                }

            console.log(profit);
    }

}


process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
    processData(_input);
});
