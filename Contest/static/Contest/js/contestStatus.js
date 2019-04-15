function Contest(questions){
    this.questionIndex = 0;
    this.score = 0;
    this.questions = questions;
}

Contest.prototype.currentIndex = function(){
    return this.questions[this.questionIndex];
}
Contest.prototype.isEnded = function(){
     return (this.questions.length <= this.questionIndex);
}
Contest.prototype.optionChosen = function(answer){

    if(this.currentIndex().isCorrect(answer))
        this.score+=4;
    else
        this.score-=2;
    this.questionIndex ++;

}
