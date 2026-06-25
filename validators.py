words_error_message = "Akceptowane są tylko liczby"
side_0_error_message = "Bok/wysokość nie może być mniejszy, bądź równy 0"

def validate_two_date(a, b, template):
  if a < 0 or b < 0:
    return render_template('template' + '.html', error_0=side_0_error_message )
  elif a == 0 or b == 0: 
    return render_template('template' + '.html', error_0=side_0_error_message)