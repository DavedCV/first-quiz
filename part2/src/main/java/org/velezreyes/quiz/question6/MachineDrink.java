package org.velezreyes.quiz.question6;

public class MachineDrink implements Drink, Cloneable {

    private final String name;
    private final boolean fizzy;
    private final double price;

    public MachineDrink(String name, boolean fizzy, double price) {
        this.name = name;
        this.fizzy = fizzy;
        this.price = price;
    }

    public Drink clone() {
        try {
            return (Drink) super.clone();
        } catch (CloneNotSupportedException e) {
            throw new RuntimeException(e);
        }
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public boolean isFizzy() {
        return fizzy;
    }

    public double getPrice() {
        return price;
    }
}
