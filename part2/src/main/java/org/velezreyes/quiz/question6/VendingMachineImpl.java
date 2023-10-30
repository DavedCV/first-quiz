package org.velezreyes.quiz.question6;

import java.util.HashMap;

public class VendingMachineImpl implements VendingMachine {

    private static VendingMachine instance = null;
    private final HashMap<String, MachineDrink> availableDrinks = new HashMap<>();

    private double currentMoney;

    private VendingMachineImpl() {
        availableDrinks.put("ScottCola", new MachineDrink("ScottCola", true, 0.75));
        availableDrinks.put("KarenTea", new MachineDrink("KarenTea", false, 1));
    }

    public static VendingMachine getInstance() {
        if (instance == null)
            instance = new VendingMachineImpl();

        return instance;
    }

    @Override
    public void insertQuarter() {
        currentMoney += 0.25;
    }

    @Override
    public Drink pressButton(String name) throws NotEnoughMoneyException, UnknownDrinkException {
        if (!availableDrinks.containsKey(name)) throw new UnknownDrinkException();

        MachineDrink targetDrink = availableDrinks.getOrDefault(name, null);
        if (currentMoney < targetDrink.getPrice()) throw new NotEnoughMoneyException();

        currentMoney -= targetDrink.getPrice();
        return targetDrink.clone();
    }
}
