package projeto;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import projeto.champions.Ahri;
import projeto.champions.Champions;
import projeto.champions.Kindred;
import projeto.champions.Lux;
import projeto.champions.Qiyana;

import javax.swing.JLabel;
import java.awt.Font;
import javax.swing.JButton;
import javax.swing.JTextField;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.GridLayout;

public class Jogo extends JFrame {

	private static final long serialVersionUID = 1L;
	private JPanel contentPane;
	private Champions[] champ = new Champions[50];

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Jogo frame = new Jogo();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public Jogo() {
		
		champ[0] = new Ahri();
		champ[1] = new Kindred();
		champ[2] = new Lux();
		champ[3] = new Qiyana();
		
		setTitle("Champions");
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 87);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		
		setContentPane(contentPane);
		contentPane.setLayout(new GridLayout(0, 4, 0, 0));
		
		for(int i = 0; i < champ.length; i++) {
			if(champ[i] == null) return;
			Champions ch = champ[i];
			JButton btnNewButton = new JButton(champ[i].getNome());
			btnNewButton.addActionListener(new ActionListener() {
				public void actionPerformed(ActionEvent e) {
					HL HLframe = new HL();
					HLframe.setVisible(true);
					HLframe.setTitle(ch.getNome());
					HLframe.Ch(ch);
					
					dispose();
				}
			});
			contentPane.add(btnNewButton);
		}
	}
}
