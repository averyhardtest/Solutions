######Stage 2a Answer
Having solved the graphic to find that we need to send a POST request to the server, a bit of guessing is required. Stage 2a reads:
> The graphic below is a puzzle, solve it to submit your answer.
> Answers which are correct will lead to the next stage of the test

It turns out that `curl -d 'answer=correct' -v averyhardtest.com/stage/2a` gives us our next clue: `{"2b":"Find Ivan's password. hint: it's not alpine"}`