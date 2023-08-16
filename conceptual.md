### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
  - PSQL is a relational database (SQL) tool to help create and store databases that can be access through the terminal

- What is the difference between SQL and PostgreSQL?
  - SQL is the language to query from relational databases, while PSQL is a specific database software that is interacted with using SQL

- In `psql`, how do you connect to a database?
  - \c <database_name>

- What is the difference between `HAVING` and `WHERE`?
  - Both are ways to filter your query to meet certain criteria, though WHERE filters at the individual row level before any aggregation takes place, whereas HAVING filters after aggregation takes place, filtering on the aggregated metric (e.g. SUM of sales)

- What is the difference between an `INNER` and `OUTER` join?
  - INNER join only returns the data where the two tables intersect, while outer joins will return all data from both tables, even for rows that can't be joined between the two tables, resulting in null values for some columns

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
  - LEFT OUTER returns all the values from the left table (ie. table specified in the FROM clause), and only returns the rows from the right table (ie. JOIN clause) that can be joined with the left tabel
  - RIGHT OUTER is the opposite

- What is an ORM? What do they do?
  - Stands for Object Relational Mapping
  - ORMs are tools that apply OOP concepts to relational databases. Specifically, rows of data from a table are handled as instances of a data class, so that they can be used in applications built on OOP principals.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
  
  Execution context and synchronicity:
    - AJAX requests are executed on the client-side (ie. on the client computer) through JS scripts, and occur asychnronously. Meaning they can occur independntly from the main execution thread - so these scripts can be run/re-run without having the reload the page.
    - Meanwhile server-side requests (like through the 'requests' library in Python) occur from the server sychronously, meaning they need to wait until they receive the response before serving up the rest of the execution thread. So from the client's perspective, if data needs to be refreshed on the page via a server-side request, this will require a page refresh.

  Cross-origin Resource sharing:
    - Cross-origin Resource sharing is a mechanism that allows a website on one URL (www.foo.com) to access data from another url (www.bar.com).
    - On the client-side (ie. through browser) CORs is not allowed for security reasons unless it is allowed by the url you're trying to access data from (www.bar.com).
    - When making a cross-origin request, the server that the request is being made to will allow the request if they include in the header: "access-control-allow-origin" whose value needs to match the origin header (ie. your website URL, www.foo.com) in the request (or be a wild-code "*")
    - There's more security risk to making request from client-side 
      - exposure of API key, auth tokens, and other sensitive info which can be viewed by anyone the through the browser on the client-side
      - code tampering and reverse-engineering by users on the client-side as the code is exposed
      - Rate limiting and abuse of requests - have more control on the server side of how many requests are made 
      - Handling errors and security responses is harder to manage on the client-side, and could potentially expose sensitive error responses and debugging info to users


- What is CSRF? What is the purpose of the CSRF token?
  - Cross-Site Request Forgery: occurs when a forged request is made to your server from a malicious website, which is disguising itself as a logged in user using a user's session token
  - For example, Alice is logged into legitbank.com and has received a session token.
  - While she's still loggged in, she receives a link from Chris (hacker) that has a link for her to win a prize. But hidden in that link is a form that makes a request to legitbank.com's server to send money to Chris' bank account, and will include Alice's session token since she's still logged in. Despite Same-origin policy, "implict cookie inclusion" by the browser still includes the session cookie with the request since it considers the cookies associated with legitbank.com as part of her browsing context.
  - A CSRF token is extra security that will be generated for a form each session she logs into her bank account and will be associated with that form.
  - legitbank.com's server is looking for this specific CSRF token to match it with her current browser session
  - Chris would not have access to this CSRF token, so cannot make malicious requests through his fake form

- What is the purpose of `form.hidden_tag()`?
  - form.hidden_tag() is a method on the form object that will apply the CSRF token to the form, though it will not be viewable to the client.
  - with this, when a form submission is made to the server, the server will look for this CSRF to validate the submission.
