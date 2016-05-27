var response = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
var grade = SpreadsheetApp.getActiveSpreadsheet().getSheets()[1];
function myFunction() {
  row  = response.getLastRow();
  sum = 0;
  ans = ["I","P","E","W","U","G","M","X",'T',"A"];
  for(i=0;i<10;i++){
    if(response.getRange(row,i+3).getValue()==ans[i]){
      sum++;
    }
  }
  response.getRange(row,24).setValue(sum);
}
