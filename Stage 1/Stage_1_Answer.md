Assuming we stumble across the site's main page, averyhardtest.com, there are 3 other pages which are trivial to navigate to. Some things stand out: A news post on October 26 states, "The great majority of people partaking have been shown very computer technical stages due to the ease of sharing a link online."
We are also challenged to find the first stage. A basic `curl -v averyhardtest.com`
reveals an ETag-Legacy header of `596f75206861766520666f756e6420537461676520312c20636f6e67726174756c6174696f6e732e0d0a0d0a46696e642075732061207072696d65206e756d6265722075726c20686967686572207468616e2037` which can be turned from a hexidecimal value into ascii text, revealing:
>You have found Stage 1, congratulations.
>Find us a prime number url higher than 7