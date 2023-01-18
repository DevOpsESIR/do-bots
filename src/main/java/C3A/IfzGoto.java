package C3A;

public class IfzGoto extends Instruction {
  private Label elseLabel;
  private Label endIfLabel;
  private Variable v;

  /**
   * If v == 0, do code until elseLabel then jump to endIfLabel
   * Else, jump to elseLabel and do code until endIfLabel
   * 
   */
  public IfzGoto(Label elseLabel, Label endIfLabel, Variable v) {
    this.elseLabel = elseLabel;
    this.endIfLabel = endIfLabel;
    this.v = v;
  }

  @Override
  public String toString() {
    return "ifz " + v + " goto " + elseLabel;
  }

  @Override
  public String toPython(Indent indent) {
    // TODO Auto-generated method stub
    return "";
  }
}