class Book
    attr_accessor :title, :author
end

book_1 = Book.new()
book_1.title = "How to be a Programmer"
book_1.author = "Singularixty"

puts "#{book_1.title} - written by #{book_1.author}"
