function update() {
    if(contest.isEnded())
    {
       finalresult();
    }
    else {
        let element = document.getElementById("Question");
        element.innerHTML = contest.currentIndex().text;
        //console.log("I  m here");
        var choices = contest.currentIndex().choices;

        for(i=0;i<choices.length;i++) {
            let element = document.getElementById("choice" +(i+1));
           // console.log(element.parentElement);
            element.innerHTML = choices[i];
            chooseButton("btn"+(i+1), choices[i]);
        }
        showCurrentQuestion()

    }

};
function finalresult(){
    var contestends="";
    contestends+="<h1>Results</h1>"+"<h2 id='score'> Your Score is: "+ contest.score +"</h2>";
    var element = document.getElementById("Contest");
    element.innerHTML =contestends;


}
function showCurrentQuestion(){

    var element = document.getElementById("QuestionNo");
    element.innerHTML = "Question "+ (contest.questionIndex+1) + " of "+ contest.questions.length;
}
function chooseButton(id,value){
    var element = document.getElementById(id);
    element.onclick = function () {
        contest.optionChosen(value);
        update();
    }

}


let questions = new Array(3);
questions[0]=("In which language semicolon at the end of the line is optional. ");
questions[1]=("Which is the fastest processing language .");
questions[2]=("In C++ which is most suitable loop when upper limit of counter variable is not given ");
let choice = new Array(3);
for(i=0;i<3;i++)
    choice[i]= new Array(4);
choice[0][0]= "C++"; choice[0][1]="Java";choice[0][2]="Python";choice[0][3]="C";
choice[1][0]= "C++"; choice[1][1]="Java";choice[1][2]="Python";choice[1][3]="Assembly Language";
choice[2][0]= "for"; choice[2][1]="while";choice[2][2]="do-while";choice[2][3]="switch";
let correctAnswer = new Array()
correctAnswer[0]="Python";
correctAnswer[1]="Assembly Language";
correctAnswer[2]="while";
var QuestionArray = [
    new Question(questions[0],["C++","Java", "Python", "C"],"Python"),
    new Question(questions[1],["C++","Java", "Python", "Assembly Language"],"Assembly Language"),
    new Question(questions[2],["for","while","do-while","switch"],"while")
];






var contest = new contest(QuestionArray);



update();
