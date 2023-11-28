package projeto.champions;

import java.util.Arrays;

import projeto.champions.quiz.Quiz;

public class Ahri extends Champions{

	@Override
	public String getNome() {
		return "Ahri";
	}

	@Override
	public String getP() {
		return "FURTO DE ESSÊNCIA\nDepois de abater 9 tropas ou monstros, Ahri se cura. Depois de eliminar um Campeão inimigo, Ahri se cura em uma quantidade ainda maior.";
	}

	@Override
	public String getQ() {
		return "ORBE DA ILUSÃO\nAhri lança e puxa de volta seu orbe, causando Dano Mágico na ida e Dano Verdadeiro na volta.";
	}

	@Override
	public String getW() {
		return "FOGO DE RAPOSA\nAhri recebe um breve impulso de Velocidade de Movimento e lança três Fogos de Raposa que perseguem e atacam inimigos próximos.";
	}

	@Override
	public String getE() {
		return "ENCANTO\nAhri manda um beijo que causa dano e encanta um inimigo, interrompendo imediatamente qualquer habilidade de movimento em progresso e fazendo com que ele ande inofensivamente em sua direção.";
	}

	@Override
	public String getR() {
		return "ÍMPETO ESPIRITUAL\nAhri avança e dispara raios de essência, causando dano a inimigos próximos. Ímpeto Espiritual pode ser conjurada até três vezes antes de entrar em Tempo de Recarga e ganha reconjurações adicionais ao eliminar Campeões inimigos.";
	}

	@Override
	public String getLore() {
		return "Ahri, uma vastaya com nove caudas, percorre um mercado exótico onde o cheiro de incenso queimado e repolho podre permeia o ar. Ela carrega duas pedras solares douradas, cuja origem desconhece, mas carrega desde sempre. Em sua busca por respostas, Ahri encontra uma vidente chamada Hirin, que reconhece as pedras como Ymelos, esculpidas por um artesão lendário chamado Ymelo. Hirin revela que as pedras podem revelar mais sobre o passado de Ahri quando reunidas em uma escultura maior.\n"
				+ "No entanto, a vidente, após oferecer chá, revela suas verdadeiras intenções de roubar uma das caudas de Ahri, considerada valiosa. Ahri, enfraquecida pelo chá, tenta resistir, mas acaba sendo imobilizada. Contudo, Ahri utiliza seus poderes de vastaya para acessar a mente de Hirin e absorver suas memórias. Ao explorar as vivências da vidente, Ahri descobre uma história de uma criança faminta escondida no mercado, momentos de apostas em uma taverna suja envolvendo uma pedra Ymelo e, por fim, o plano de Hirin para roubar a cauda de Ahri.\n"
				+ "À medida que Ahri consome as memórias de Hirin, recupera sua força e habilidade de se mover. A vidente, agora privada de algumas memórias, acorda sem lembrar do encontro com Ahri. A ira da vastaya se dissipa, e ela parte do mercado com um novo conhecimento: o nome Ymelo e a imagem de um homem com sobrancelhas em forma de asas.";
	}

	
	/*
	 * HISTORIA DA AHRI
	 * Ahri, uma vastaya com nove caudas, percorre um mercado exótico onde o cheiro de incenso queimado e repolho podre permeia o ar.
	 * Ela carrega duas pedras solares douradas, cuja origem desconhece, mas carrega desde sempre.
	 * Em sua busca por respostas, Ahri encontra uma vidente chamada Hirin, que reconhece as pedras como Ymelos, esculpidas por um artesão lendário chamado Ymelo.
	 * Hirin revela que as pedras podem revelar mais sobre o passado de Ahri quando reunidas em uma escultura maior.
	 * 
	 * No entanto, a vidente, após oferecer chá, revela suas verdadeiras intenções de roubar uma das caudas de Ahri, considerada valiosa.
	 * Ahri, enfraquecida pelo chá, tenta resistir, mas acaba sendo imobilizada.
	 * Contudo, Ahri utiliza seus poderes de vastaya para acessar a mente de Hirin e absorver suas memórias.
	 * Ao explorar as vivências da vidente, Ahri descobre uma história de uma criança faminta escondida no mercado, momentos de apostas em uma taverna suja envolvendo uma pedra Ymelo e, por fim, o plano de Hirin para roubar a cauda de Ahri.
	 * 
	 * À medida que Ahri consome as memórias de Hirin, recupera sua força e habilidade de se mover.
	 * A vidente, agora privada de algumas memórias, acorda sem lembrar do encontro com Ahri.
	 * A ira da vastaya se dissipa, e ela parte do mercado com um novo conhecimento: o nome Ymelo e a imagem de um homem com sobrancelhas em forma de asas.
	 */
	
	@Override
	public Quiz[] getQuiz() {
		Quiz[] quizes = new Quiz[4];
		/*
		 * Pergunta: Qual é o objetivo inicial de Ahri ao percorrer o mercado exótico?
		 * 	Encontrar comida para saciar sua fome.
		 * 	Descobrir a origem e significado das pedras solares douradas.
		 * Resposta correta: Descobrir a origem e significado das pedras solares douradas.
		 * 
		 * Pergunta: Por que Hirin oferece chá a Ahri durante o encontro no mercado?
		 *	Para fortalecer os poderes de Ahri.
		 * 	Com a intenção de enfraquecer Ahri e roubar uma de suas caudas.
		 * Resposta correta: Com a intenção de enfraquecer Ahri e roubar uma de suas caudas.
		 * 
		 * Pergunta: Qual é a revelação mais significativa obtida por Ahri ao absorver as memórias de Hirin?
		 *	A história de uma criança escondida no mercado.
		 * 	O plano de Hirin para apostar em uma taverna suja.
		 * Resposta correta: A história de uma criança escondida no mercado.
		 * 
		 * Pergunta: Como Ahri recupera sua força e habilidade de se mover após ser enfraquecida pelo chá de Hirin?
		 * 	Bebendo uma poção mágica.
		 * 	Absorvendo as memórias de Hirin através de seus poderes de vastaya.
		 * Resposta correta: Absorvendo as memórias de Hirin através de seus poderes de vastaya.
		 */
		String[] p1 = {"Encontrar comida para saciar sua fome.", "Descobrir a origem e significado das pedras solares douradas."};
		Quiz quiz = new Quiz("Qual é o objetivo inicial de Ahri ao percorrer o mercado exótico?", "Descobrir a origem e significado das pedras solares douradas.", p1, 5) ;
		quizes[0] = quiz;
		String[] p2 = {"Para fortalecer os poderes de Ahri.", "Com a intenção de enfraquecer Ahri e roubar uma de suas caudas."};
		quiz = new Quiz("Por que Hirin oferece chá a Ahri durante o encontro no mercado?", "Com a intenção de enfraquecer Ahri e roubar uma de suas caudas.", p2, 5);
		quizes[1] = quiz;
		String[] p3 = {"A história de uma criança escondida no mercado.", "O plano de Hirin para apostar em uma taverna suja."};
		quiz = new Quiz("Qual é a revelação mais significativa obtida por Ahri ao absorver as memórias de Hirin?", "A história de uma criança escondida no mercado.", p3, 5);
		quizes[2] = quiz;
		String[] p4 = {"Bebendo uma poção mágica.", "Absorvendo as memórias de Hirin através de seus poderes de vastaya."};
		quiz = new Quiz("Como Ahri recupera sua força e habilidade de se mover após ser enfraquecida pelo chá de Hirin?", "Absorvendo as memórias de Hirin através de seus poderes de vastaya.", p4, 5);
		quizes[3] = quiz;
		

		return quizes;
	}

}
