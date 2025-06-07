const calendar_display=(year,month)=>{
    console.log("      "+month+"月"+" "+year);
    const weeks=["日","月","火","水","木","金","土"];
    console.log(weeks.join(" "));
    const startday=new Date(year,month-1,1).getDay();
    
    const monthdays=new Date(year,month,0).getDate();

    const result = [];
    const blank=String(" ").padStart(2," ");
    for (let index = 0; index < startday; index++) {
      result.push(blank);
    }
for (let i = 1; i <= monthdays; i++) {
    const weekinput=startday+i;
    const day=String(i).padStart(2," ");
    result.push(day);

    if(weekinput%7==0){
      console.log(result.join(" "));
      result.length=0;
     }
}
if(result.length>0){
  console.log(result.join(" "));

}

console.log(" ");
}


const arg=process.argv.splice(2);
const year=new Date().getFullYear();
let month;
if(arg[0]=="-m"&&arg[1]>=1&&arg[1]<=12){
  month=arg[1];

calendar_display(year,month);
}else if(arg[0]=="-m"&& (arg[1]<1||arg[1]>12 || arg[1]!==" ")){
  console.log("不正な入力値です。")
  
}else{
  arg[1]=new Date().getMonth();
  month=arg[1]+1;
  calendar_display(year,month);
}


